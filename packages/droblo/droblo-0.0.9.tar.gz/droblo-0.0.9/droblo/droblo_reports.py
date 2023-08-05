# coding=utf-8
"""
Report generation
"""
import argparse
import socket
import sys
import logging
from pathlib import Path
from collections import OrderedDict
from pap_logger import *
from sqlalchemy.exc import OperationalError

from droblo.ORM.droblo_ORM import get_session, DrobloBroadException
from droblo.filesystem.droblo_fs import load_connection_string
from droblo.ORM.droblo_reports_ORM import DrobloReports

__REPORT_EXT__ = ["csv"]


def parse_arguments():
    """
    parse cli arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='File system watcher inserting files info to DB.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-a", "--all", help="Report on all hosts.", action="store_true")
    parser.add_argument("-A", "--ALL", help="Report on all hosts, one file per host.", action="store_true")
    parser.add_argument("-r", "--reports_path", help="Path where to store reports.", type=Path)
    parser.add_argument("-t", "--reports_type", help="Reports type.", choices=__REPORT_EXT__, default="csv")

    parser.add_argument("-v", "--verbose", help="Verbose.", action="store_true")
    parser.add_argument("-d", "--debug", help="Debugging.", action="store_true")
    parser.add_argument("-l", "--log_file", help="Path to log file.", type=Path)
    parser.add_argument("-sh", "--syslog_host", help="Syslog hostname.", type=str)
    parser.add_argument("-sp", "--syslog_port", help="Syslog port.", type=int, default=514)
    return parser.parse_args()


def main():
    """
    Droblo_reports entry point
    """
    args = parse_arguments()
    try:
        pap = PaPLogger(verbose_fmt=True, logfile_with_hostname=True)
        pap.level = DEBUG if args.debug else INFO
        pap.verbose_fmt = args.verbose
        pap.log_file = args.log_file
        pap.syslog_port = args.syslog_port
        pap.syslog_host = args.syslog_host
        try:
            session = get_session(connection_string=load_connection_string(), echo=args.debug)
            split_by_host = True if args.ALL else False
            reports = Reports(session=session, all=args.all)
            reports.get_results()
            reports.generate_reports(extension=args.reports_type,
                                     split_by_host=split_by_host,
                                     reports_path=args.reports_path)
        except OperationalError:
            logging.error(msg="Connection to database failed.")
            sys.exit(-1)
    except KeyboardInterrupt:
        logging.info("Exiting")
        sys.exit(0)
    except DrobloBroadException:
        logging.exception("Other exception. To investigate")
        logging.shutdown()
        sys.exit(-1)


class Reports:
    """
    Get data and generates reports
    """

    def __init__(self, session, all: bool):
        self.dr = DrobloReports(session=session)
        self.all = all
        self.host = socket.gethostname()
        self.reports = OrderedDict()
        self.hosts = self.dr.get_list_hosts(as_list=True) if self.all else []

    def get_results(self):
        """
        Get pandas DataFrame
        """
        if self.all:
            self.reports["Hosts"] = self.dr.get_list_hosts()
            self.reports["Hosts with inactive watchers"] = self.dr.get_inactive_watchers()
        dup = self.dr.get_duplicated_files() if self.all else self.dr.get_duplicated_files(host=self.host)
        self.reports["Duplicated files"] = dup
        ds = self.dr.get_potential_disk_space_savings() if self.all else self.dr.get_potential_disk_space_savings(host=self.host)
        self.reports["Potential disk space saving"] = ds

    def generate_reports(self, extension: str, reports_path: Path, split_by_host: bool):
        for name, df in self.reports.items():
            print(name)
            print()
            print(df)
            print()
            print()


if __name__ == "__main__":
    main()
