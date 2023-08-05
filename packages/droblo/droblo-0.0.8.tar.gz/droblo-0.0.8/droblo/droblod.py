#!/usr/bin/python3
# coding=utf-8
"""
Droblod is a filesystem watcher that will take checksum of all new files, insert them in DB
"""

from pap_logger import *
import argparse
import signal
import threading
import time

from pathlib import Path
from datetime import datetime

from watchdog.observers import Observer

from droblo.postgreSQL_poller.drobloPostgreSQLPoller import DrobloPostgreSQLPoller
from droblo.ORM.droblo_ORM import *
from droblo.filesystem.droblo_fs import get_recursive_file_list, get_file_dict, str_dict_to_path_dict, \
    get_connection_string, logon_start_install, logon_start_install_src_dst


# TODO: decide and implement how to handle paths data watch folders being moved, removed or renamed

class RestartWatcher(BaseException):
    """
    This exception is used to restart the watcher.
    """

    def __init__(self):
        super().__init__()


def recursively_str(r: bool):
    return " recursively" if r else ""


class DrobloWatcher:
    """
    Droblo Watcher class
    """
    observer = None
    no_signal = None

    def __init__(self, main_args):
        self.args = main_args
        self.host = socket.gethostname()
        self.session = get_session_from_args_or_conf(self.args)
        self.sqlite_session = get_sqlite_session()

        if self.session:
            self.paths = get_paths_from_args_or_session(self.args, self.session)
            self.excluded_paths = get_excluded_from_args_or_session(self.args, self.session)
            save_paths_to_db(self.session, self.args, self.paths, self.excluded_paths)
        else:
            self.paths = get_paths_from_args_or_session(self.args, self.sqlite_session)
            self.excluded_paths = get_excluded_from_args_or_session(self.args, self.sqlite_session)
        save_paths_to_db(self.sqlite_session, self.args, self.paths, self.excluded_paths)

        self.paths = str_dict_to_path_dict(self.paths)
        self.excluded_paths = str_dict_to_path_dict(self.excluded_paths)

        signal.signal(signal.SIGUSR2, self._reload)
        self.poller = None
        self.restart_watch = False
        self.status_dict = None

    def _end_watch(self):
        self.restart_watch = True
        raise RestartWatcher

    def _reload(self, signum, _):
        """
        restart the watchdog
        """
        logging.info("Reloading config (signal %s received)" % signum)
        postgre_session = get_session_from_args_or_conf(self.args)
        upsert_sqlite_data_to_postgresql(host=self.host, sqlite_session=self.sqlite_session,
                                         postgre_session=postgre_session)
        self._end_watch()

    def _start_poller(self):
        logging.info("Starting the poller")
        do_poll = threading.Event()
        connection_string = get_connection_string(self.args, obfuscated=True)
        self.poller = DrobloPostgreSQLPoller(connection_string=connection_string,
                                             droblo_poll=do_poll, interval=self.args.interval)
        do_poll.set()
        self.poller.start()
        return do_poll

    def watch(self):
        """
        Starts the watchdog. All files info are updated in DB upon FS event.
        """

        if DrobloStatus(self.sqlite_session).is_watcher_running(self.host):
            logging.critical("The watcher is already running on %s." % self.host)
            sys.exit(1)

        do_poll = self._start_poller()
        self.no_signal = True
        event_handler = PostgresEventHandler(self.session, self.sqlite_session, self.paths, self.excluded_paths)
        self.observer = Observer()
        exception_raised = False

        for path, recursive in self.paths.items():
            if path.exists():
                logging.info("Adding %s to the list of%s watched folders." % (path, recursively_str(r=recursive)))
                for xp in self.excluded_paths:
                    if path in xp.parents:
                        logging.info("\tEvents triggered under %s are ignored%s." % (xp, recursively_str(r=recursive)))
                self.observer.schedule(event_handler, str(path), recursive=recursive)
            else:
                logging.warning("Skipping %s : path does not exists." % path)

        try:
            self.observer.start()
        except OSError:
            logging.error("Permission denied on one of the given paths. Exiting.")
            sys.exit(-1)

        try:
            self._initialize_status_table()
        except DrobloBroadException:
            logging.critical("Unable to initialize the status table")
            sys.exit(-1)

        try:
            status_watchdog = 0
            while self.no_signal:
                if status_watchdog == 20:
                    self._heartbeat_status()
                    status_watchdog = 0
                time.sleep(0.5)
                status_watchdog += 1
        except RestartWatcher:
            logging.info("Stopping the observer (restart request)")
            if self.sqlite_session.info.get('has_flushed', False):
                self.sqlite_session.commit()
            if self.session.info.get('has_flushed', False):
                self.session.rollback()
            self.observer.stop()
        except KeyboardInterrupt:
            logging.info("Stopping the observer (KeyboardInterrupt)")
            self.observer.stop()
        except DrobloBroadException:
            logging.exception("Unknown exception")
            exception_raised = True
        finally:
            logging.info("Exiting watch %s" % (" in error" if exception_raised else ""))
            self.observer.join()
            logging.debug("Observer joined")
            do_poll.clear()
            if not self.restart_watch:
                self._exit_droblod(exception_raised)
            else:
                self.restart_watch = False
                self.session = get_session_from_args_or_conf(self.args)
                self.watch()

    def _exit_droblod(self, exception_raised):
        logging.info("Exiting droblod.")
        self.status_dict["end_time"] = datetime.now()
        DrobloStatus(self.session, self.status_dict)
        DrobloStatus(self.sqlite_session, self.status_dict)
        logging.debug("Status table cleaned.")
        sys.exit(-1 if exception_raised else 0)

    def _heartbeat_status(self):
        self.status_dict["update_time"] = datetime.now()
        DrobloStatus(self.session, self.status_dict)
        DrobloStatus(self.sqlite_session, self.status_dict)
        logging.debug("Heartbeat sent on Status table.")

    def _initialize_status_table(self):
        self.status_dict = {"host": self.host,
                            "status": "watch",
                            "start_time": datetime.now(),
                            "update_time": datetime.now(),
                            "end_time": None
                            }
        DrobloStatus(self.session, self.status_dict)
        DrobloStatus(self.sqlite_session, self.status_dict)
        logging.debug("Status table initialized.")

    def show_config(self):
        """
        Displays information about the current setup on the command line
        """
        print()
        print("The database connection string is :")
        print("\t%s" % get_connection_string(self.args, obfuscated=True))
        print()
        if len(self.paths):
            print("The following paths are being watched:")
            for path, recursive in self.paths.items():
                print("\t%s%s" % (path, recursively_str(r=recursive)))
        else:
            print("No paths are being watched")
        print()
        if len(self.excluded_paths):
            print("The following paths are excluded:")
            for path, recursive in self.excluded_paths.items():
                print("\t%s%s" % (path, recursively_str(r=recursive)))
        else:
            print("No paths are excluded")

    def populate(self):
        """
        recursively parse all files in all paths, removing excluded paths from DB.
        :return:
        """
        if not self.session:
            logging.critical("Populate mode requires connectivity to the PostgreSQL server.")
            sys.exit(-1)

        status_dict = {"host": self.host,
                       "status": "populate",
                       "start_time": datetime.now(),
                       "update_time": None,
                       "end_time": None
                       }

        DrobloStatus(self.session, status_dict)
        if not DrobloStatus(self.session).is_clean(self.host):
            logging.warning("The watcher is not running.")
            logging.warning("It is highly recommended to populate while it is active.")

        file_count = 0
        for path, recursive in self.paths.items():
            if recursive:
                fl = get_recursive_file_list(path, self.excluded_paths)
            else:
                fl = [x for x in Path(path).iterdir() if not x.is_dir()]
            for file in fl:
                logging.info("Populating : %s" % file)
                try:
                    data = get_file_dict(str(file))
                    data["host"] = self.host
                    Files(self.session, data)
                    file_count += 1
                except FileNotFoundError:
                    pass
                except DrobloBroadException:
                    logging.exception("Other exception. To investigate")
        for excluded in self.excluded_paths.keys():
            Files(self.session, {"host": self.host, "deleted": excluded})
        status_dict["end_time"] = datetime.now()
        DrobloStatus(self.session, status_dict)
        return file_count


def _logon_start_install_help():
    src, install_path = logon_start_install_src_dst(root=Path(__file__).parent)
    if sys.platform == 'linux':
        return f"Installs systemd unit file {src} to {install_path}"
    elif sys.platform == 'darwin':
        return f"Installs plaunchd plist file {src} to {install_path}"
    elif sys.platform == 'win32':
        return f"Registers scheduled task {src} to the windows task scheduler."
    else:
        return f"logon_start for {sys.platform} is not implemented at the moment."


def parse_arguments():
    """
    parse cli arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='File system watcher inserting files info to DB.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-H", "--db_host", help="Database server hostname", default="localhost", type=str)
    parser.add_argument("-P", "--db_port", help="Database server port", default="5432", type=int)
    parser.add_argument("-N", "--db_name", help="Database name", default="droblo", type=str)
    parser.add_argument("-U", "--db_username", help="Database username", default="droblo", type=str)
    parser.add_argument("-W", "--db_password", help="Database password", type=str)
    parser.add_argument("-i", "--interval", help="Database server polling interval in seconds", type=int, default=3)

    parser.add_argument("-p", "--paths",
                        help="Paths to watch. If none is given, will use the values in table paths.\n"
                             "One can specify the path recursivity by suffixing it with ',1'.\n"
                             "Recursivity is off by default for watch paths.", nargs='+', type=str)
    parser.add_argument("-x", "--excluded",
                        help="Paths to exclude from the watch. If none is given, will use the values in table paths.\n"
                             "One can specify the path non-recursivity by suffixing it with ',0'\n"
                             "Recursivity is on by default for exclusion paths.", nargs='+', type=str)
    parser.add_argument("-s", "--save", help="Insert or update given paths in DB.", action="store_true")
    parser.add_argument("-S", "--purge_and_save", help="Purge then insert given paths in DB.", action="store_true")
    parser.add_argument("--show_config", help="Displays the current configuration.", action="store_true")
    parser.add_argument("--populate", help="Populate the database in non-watching mode.", action="store_true")
    parser.add_argument("--logon_start", help=_logon_start_install_help(), action="store_true")
    parser.add_argument("-v", "--verbose", help="Verbose (logs events information).", action="store_true")
    parser.add_argument("-d", "--debug", help="Debugging (logs debugging information).", action="store_true")
    parser.add_argument("-l", "--log_file", help="Path to log file.", type=Path)
    parser.add_argument("-sh", "--syslog_host", help="Syslog hostname.", type=str)
    parser.add_argument("-sp", "--syslog_port", help="Syslog port.", type=int, default=514)
    return parser.parse_args()


def main():
    """
    Droblo entry point
    """
    args = parse_arguments()
    try:
        pap = PaPLogger(verbose_fmt=True, logfile_with_hostname=True)
        pap.level = DEBUG if args.debug else INFO
        pap.verbose_fmt = args.verbose
        pap.log_file = args.log_file
        pap.syslog_port = args.syslog_port
        pap.syslog_host = args.syslog_host

        if args.logon_start:
            logon_start_install(root=Path(__file__).parent)

        if args.populate:
            logging.info("Starting to populate")
            start_time = datetime.now()
            files_count = DrobloWatcher(args).populate()
            end_time = datetime.now()
            logging.info("Checked %d files in %s" % (files_count, (end_time - start_time)))
        elif args.show_config:
            DrobloWatcher(args).show_config()
        else:
            logging.info("Starting to watch")
            while True:
                DrobloWatcher(args).watch()
                logging.info("Force restarting the watcher. Pretty bad")
    except KeyboardInterrupt:
        logging.info("Exiting (KeyboardInterrupt)")
        sys.exit(0)
    except DrobloBroadException:
        logging.exception("Other exception. To investigate")
        logging.shutdown()
        sys.exit(-1)


if __name__ == "__main__":
    main()
