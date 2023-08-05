# coding=utf-8
"""
This modules handles everything DB related for this project
"""
import logging
import socket
import sys

from sqlalchemy import create_engine
from sqlalchemy import Column, Index
from sqlalchemy import Integer, String, DateTime, Boolean, BigInteger, BLOB
from sqlalchemy import update, func, delete, insert

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.dialects.postgresql import insert as pginsert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.elements import True_, False_
from sqlalchemy.exc import OperationalError, ResourceClosedError

from watchdog.events import FileSystemEventHandler, FileCreatedEvent

from droblo.filesystem.droblo_fs import get_file_dict, get_recursive_file_list, is_excluded, get_config_path, \
    get_connection_string, dump_connection_string

Base = declarative_base()

__SECONDS_THRESHOLD_FOR_CLEAN__ = 11
__PSYCOPG2__ = 'psycopg2'


class DrobloBroadException(BaseException):
    """
    BaseException override for pep8 compliance.
    """

    def __init__(self):
        super().__init__()


class DrobloConnectivityLostException(DrobloBroadException):
    """
        BaseException override for pep8 compliance.
        """

    def __init__(self):
        super().__init__()


def get_session_driver_name(session):
    return session.bind.dialect.driver


def get_session(connection_string: str, echo=False, pool_pre_ping=True):
    """
    return SQLAlchemy session object.
    :param pool_pre_ping:
    :param connection_string:
    :param echo:
    :return:
    """
    engine = create_engine(connection_string, echo=echo, pool_pre_ping=pool_pre_ping)
    session_obj = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    session = session_obj()
    session.connection()
    return session


def get_sqlite_session(echo=False):
    droblo_db = get_config_path() / 'droblo.db'

    return get_session(connection_string=f"sqlite:///{droblo_db}", echo=echo, pool_pre_ping=False)


def get_session_from_args_or_conf(main_args):
    """
    watch and populate common values handling.
    :param main_args:
    :return:
    """
    conn_str = get_connection_string(main_args)
    try:
        session = get_session(connection_string=conn_str, echo=main_args.debug)
    except OperationalError:
        obfuscated_conn_str = get_connection_string(main_args, obfuscated=True)
        logging.error(msg="Connection to database failed. Connection string was %s" % obfuscated_conn_str)
        logging.warning(msg="Falling back to sqlite only.")
        session = None
    else:
        dump_connection_string(conn_str)

    return session


def files_to_dict(f, deleted_files=False):
    if deleted_files:
        return {"deleted": f.file, "host": f.host}
    return {"file": f.file, "hash": f.hash, "host": f.host, "size": f.size, "mtime": f.mtime, "atime": f.atime,
            "ctime": f.ctime}


def get_excluded_from_args_or_session(main_args=None, session=None):
    if not main_args or not main_args.excluded:
        excluded_paths = Paths().get_excluded_paths(session)
    else:
        excluded_paths = {}
        for p in main_args.excluded:
            p_split = p.split(",")
            if len(p_split) > 1:
                excluded_paths[p_split[0]] = bool(p_split[1])
            else:
                excluded_paths[p] = True
    return excluded_paths


def get_paths_from_args_or_session(main_args=None, session=None):
    if not main_args or not main_args.paths:
        paths = Paths().get_watch_paths(session)
    else:
        paths = {}
        for p in main_args.paths:
            p_split = p.split(",")
            if len(p_split) > 1:
                paths[p_split[0]] = bool(p_split[1])
            else:
                paths[p] = False
    if not paths:
        logging.error("no paths configured; specify then on the command line")
        sys.exit(1)

    return paths


def upsert_sqlite_data_to_postgresql(host, sqlite_session, postgre_session):
    try:
        sqlite_paths = get_paths_from_args_or_session(session=sqlite_session)
        sqlite_excluded = get_excluded_from_args_or_session(session=sqlite_session)
        logging.info("Updating PostgreSQL paths table using sqlite paths table.")
        Paths().save_paths(postgre_session, paths=sqlite_paths, excluded=sqlite_excluded, purge=True)
    except OperationalError:
        logging.exception("Ouch OperationalError")
    except DrobloBroadException:
        logging.exception("Ouch DrobloBroadException")

    try:
        logging.info("Updating files table for new and updated files.")
        max_mod_time = postgre_session.query(func.max(Files.mtime)).filter(Files.host == host).scalar()
        sqlite_files_q = sqlite_session.query(Files).filter(Files.host == host)
        if max_mod_time:
            logging.info(f"The last modification time in PostgreSQL is {max_mod_time}")
            sqlite_files_q = sqlite_files_q.filter(Files.host >= max_mod_time)
        files_data = sqlite_files_q.all()
        logging.info(f"Inserting {len(files_data)} entries from sqlite to PostgreSQL.")
        Files(postgre_session, [files_to_dict(f) for f in files_data])
        logging.info(f"Cleaning up sqlite files table.")
        sqlite_session.execute(delete(Files))
    except (OperationalError, ResourceClosedError):
        logging.exception("Ouch (OperationalError,ResourceClosedError). Rolling back.")
        sqlite_session.rollback()
    except DrobloBroadException:
        logging.exception("Ouch DrobloBroadException. Rolling back.")
        sqlite_session.rollback()

    try:
        logging.info("Updating files table for deleted files")
        deleted_files_data = sqlite_session.query(DeletedFiles).filter(DeletedFiles.host == host).all()
        logging.info(f"Deleting {len(deleted_files_data)} entries from sqlite to PostgreSQL.")
        Files(postgre_session).delete_from_list([files_to_dict(f, True) for f in deleted_files_data])
        logging.info(f"Cleaning up sqlite deleted_files table.")
        sqlite_session.execute(delete(DeletedFiles))
    except (OperationalError, ResourceClosedError):
        logging.exception("Ouch (OperationalError,ResourceClosedError). Rolling back.")
        sqlite_session.rollback()
    except DrobloBroadException:
        logging.exception("Ouch DrobloBroadException. Rolling back.")
        sqlite_session.rollback()


def save_paths_to_db(session, main_args, paths, excluded_paths):
    # if not session or session.bind.engine.connection.closed:
    if not session:
        logging.warning("No session or session is disconnected")
        return
    if main_args.save or main_args.purge_and_save:
        purge = True if main_args.purge_and_save else False
        Paths().save_paths(session, paths, excluded_paths, purge)
        logging.info("New paths configuration saved.")


class PostgresEventHandler(FileSystemEventHandler):
    """
    Implemented on top of watchdog FileSystemEventHandler, handles captures events to DB (via Files and Paths classes).
    """

    def __init__(self, session, sqlite_session, paths, excluded_paths):

        self.session = session
        self.sqlite_session = sqlite_session
        self.host = socket.gethostname()
        self.paths = paths
        self.excluded = excluded_paths

    @staticmethod
    def _get_what(event) -> str:
        return 'directory' if event.is_directory else 'file'

    def _send_recursive_fake_created_events(self, path):
        """
        Force created events (used when destination of on_moved is not excluded.)
        :param path:
        """
        for file in get_recursive_file_list(path, self.excluded):
            FileCreatedEvent(file)

    def on_moved(self, event):
        """
        watchdog file moved event handling.
        :param event:
        :return:
        """
        if is_excluded(event.dest_path, self.excluded):
            # in case the exclusion list was updated
            if self.session:
                try:
                    Files(self.session, {"host": self.host, "deleted": event.src_path})
                except DrobloConnectivityLostException:
                    # self.session.remove()
                    self.session = None
            Files(self.sqlite_session, {"host": self.host, "deleted": event.src_path})
            logging.debug("Deleting %s as its destination is in the exclusion list" % event.dest_path)
        elif is_excluded(event.src_path, self.excluded):
            logging.debug("Forcing created event %s as it is in the exclusion list" % event.src_path)
            if event.is_directory:
                self._send_recursive_fake_created_events(event.src_path)
            else:
                self.on_created(event)
        else:
            data = {"host": self.host, "src": event.src_path, "dst": event.dest_path}
            action = 'moved_dir' if event.is_directory else 'moved_file'
            data[action] = ""
            if self.session:
                try:
                    Files(self.session, data)
                except DrobloConnectivityLostException:
                    # self.session.remove()
                    self.session = None
            Files(self.sqlite_session, data)
            logging.info("Moved %s: from %s to %s", self._get_what(event), event.src_path, event.dest_path)

        if event.src_path in self.paths.keys():
            if is_excluded(event.dest_path, self.excluded):
                logging.debug("Removing %s from the config as it was moved to an excluded path" % event.src_path)
                if self.session:
                    Paths().delete_path(self.session, path=event.src_path)
                Paths().delete_path(self.sqlite_session, path=event.src_path)
            else:
                logging.info("Updating %s in the config" % event.src_path)
                if self.session:
                    Paths().update_path(self.session, src=event.src_path, dst=event.dest_path, excluded=False)
                Paths().update_path(self.sqlite_session, src=event.src_path, dst=event.dest_path, excluded=False)

        if event.src_path in self.excluded.keys():
            logging.debug("Updating %s in the config" % event.src_path)
            if self.session:
                Paths().update_path(self.session, src=event.src_path, dst=event.dest_path, excluded=True)
            Paths().update_path(self.sqlite_session, src=event.src_path, dst=event.dest_path, excluded=True)

    def on_created(self, event):
        """
        watchdog file created event handling
        :param event:
        :return:
        """
        what = self._get_what(event)

        if is_excluded(event.src_path, self.excluded):
            # in case the exclusion list was updated
            if self.session:
                try:
                    Files(self.session, {"host": self.host, "deleted": event.src_path})
                except DrobloConnectivityLostException:
                    # self.session.remove()
                    self.session = None
            Files(self.sqlite_session, {"host": self.host, "deleted": event.src_path})
            logging.debug("Deleting %s as it is in the exclusion list" % event.src_path)
            return

        if what == 'file':
            try:
                data = get_file_dict(event.src_path)
                data["host"] = self.host
                if self.session:
                    try:
                        Files(self.session, data)
                    except DrobloConnectivityLostException:
                        # self.session.remove()
                        self.session = None
                Files(self.sqlite_session, data)
            except FileNotFoundError:
                return
        logging.info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        """
        watchdog file deleted event handling
        :param event:
        """
        if self.session:
            try:
                Files(self.session, {"host": self.host, "deleted": event.src_path})
            except DrobloConnectivityLostException:
                # # self.session.remove()
                self.session = None
        Files(self.sqlite_session, {"host": self.host, "deleted": event.src_path})
        if is_excluded(event.src_path, self.excluded):
            logging.debug("Not logging %s as it is in the exclusion list" % event.src_path)
        else:
            logging.info("Deleted %s: %s", self._get_what(event), event.src_path)

        if event.src_path in self.paths.keys():
            logging.info("Deleting %s from the config as well" % event.src_path)
            if self.session:
                Paths().delete_path(self.session, path=event.src_path)
            Paths().delete_path(self.sqlite_session, path=event.src_path)

        if event.src_path in self.excluded.keys():
            logging.debug("Leaving %s in the config as we want to prevent it being watched if is later re-created")

    def on_modified(self, event):
        """
        watchdog file modified event handling
        :param event:
        :return:
        """
        what = self._get_what(event)

        if is_excluded(event.src_path, self.excluded):
            # in case the exclusion list was updated
            if self.session:
                try:
                    Files(self.session, {"host": self.host, "deleted": event.src_path})
                except DrobloConnectivityLostException:
                    # self.session.remove()
                    self.session = None
            Files(self.sqlite_session, {"host": self.host, "deleted": event.src_path})
            logging.debug("Deleting %s as it is in the exclusion list" % event.src_path)
        elif what == 'file':
            try:
                data = get_file_dict(event.src_path)
                data["host"] = self.host
                if self.session:
                    try:
                        Files(self.session, data)
                    except DrobloConnectivityLostException:
                        # self.session.remove()
                        self.session = None
                Files(self.sqlite_session, data)
                logging.info("Modified %s: %s", what, event.src_path)
            except FileNotFoundError:
                return
        else:
            # We don't store info on directories
            pass

        # if event.src_path in self.paths.keys():
        #     src = Path(event.src_path)
        #     dst = Path(event.dest_path)
        #     if src.parent == dst.parent:
        #         logging.info("Updating %s in the config" % event.src_path)
        #         Paths().update_paths(self.session, src=event.src_path, dst=event.dest_path, excluded=False)
        #
        # if event.src_path in self.excluded.keys():
        #     src = Path(event.src_path)
        #     dst = Path(event.dest_path)
        #     if src.parent == dst.parent:
        #         logging.debug("Updating %s in the config" % event.src_path)
        #         Paths().update_paths(self.session, src=event.src_path, dst=event.dest_path, excluded=True)


class Paths(Base):
    """
    Paths
    Table where we store the different hosts configuration regarding watch or exclusion paths along a recursivity flag.
    Not to be confounded with pathlib Path (which we make sure to not use in this file for this exact reason)
    """
    __tablename__ = 'paths'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String, nullable=False, unique=False)
    path = Column(String, nullable=False, unique=False)
    recursive = Column(Boolean, nullable=False, unique=False)
    excluded = Column(Boolean, nullable=False, unique=False)
    paths_index = Index("paths_index", host, path, unique=True)

    @staticmethod
    def get_watch_paths(session):
        """
        :param session:
        :return:
        """
        if not session:
            logging.warning("No session or session is disconnected")
            return

        return dict(session.query(Paths.path, Paths.recursive).
                    filter(Paths.host == socket.gethostname()).
                    filter(Paths.excluded == False_()).all())

    @staticmethod
    def get_excluded_paths(session):
        """

        :param session:
        :return:
        """
        if not session:
            logging.warning("No session or session is disconnected")
            return

        return dict(session.query(Paths.path, Paths.recursive).
                    filter(Paths.host == socket.gethostname()).
                    filter(Paths.excluded == True_()).all())

    @staticmethod
    def save_paths(session, paths, excluded, purge):
        """
        insert or update into status
        :param purge:
        :param excluded:
        :param paths:
        :param session:
        """

        if not session:
            logging.warning("No session or session is disconnected")
            return

        host = socket.gethostname()
        if purge:
            delete_stmt = delete(Paths).where(Paths.host == host)
            session.execute(delete_stmt)
        if get_session_driver_name(session) == __PSYCOPG2__:
            for path, recursive in paths.items():
                insert_stmt = pginsert(Paths).values(host=host, path=path, recursive=recursive, excluded=False)
                update_stmt = insert_stmt.on_conflict_do_update(
                    index_elements=Paths.paths_index.columns, set_=dict(recursive=recursive, excluded=False)
                )
                session.execute(update_stmt)

            for path, recursive in excluded.items():
                insert_stmt = pginsert(Paths).values(host=host, path=path, recursive=recursive, excluded=True)
                update_stmt = insert_stmt.on_conflict_do_update(
                    index_elements=Paths.paths_index.columns, set_=dict(recursive=recursive, excluded=True)
                )
                session.execute(update_stmt)
        else:
            for path, recursive in paths.items():
                delete_stmt = delete(Paths).where(Paths.host == host). \
                    where(Paths.path == path).where(Paths.excluded.is_(False))
                insert_stmt = insert(Paths).values(host=host, path=path, recursive=recursive, excluded=False)

                session.execute(delete_stmt)
                session.execute(insert_stmt)

            for path, recursive in excluded.items():
                delete_stmt = delete(Paths).where(Paths.host == host). \
                    where(Paths.path == path).where(Paths.excluded.is_(True))
                insert_stmt = insert(Paths).values(host=host, path=path, recursive=recursive, excluded=True)

                session.execute(delete_stmt)
                session.execute(insert_stmt)

        try:
            session.commit()
        except (OperationalError, ResourceClosedError):
            logging.exception("Rolling back save_paths ((OperationalError,ResourceClosedError))")
            session.rollback()
        except DrobloBroadException:
            logging.exception("Rolling back save_paths (DrobloBroadException)")
            session.rollback()

    @staticmethod
    def update_path(session, src: str, dst: str, excluded: bool):
        """
        Update paths in the config (called following on_modifed event)
        :param session:
        :param src:
        :param dst:
        :param excluded:
        """
        if not session:
            logging.warning("No session or session is disconnected")
            return

        host = socket.gethostname()

        update_path_stmt = update(Paths).values(path=dst). \
            where(Paths.host == host).where(Paths.path == src).where(Paths.excluded is excluded)
        session.execute(update_path_stmt)

        try:
            session.commit()
        except (OperationalError, ResourceClosedError):
            logging.exception("Rolling back update_path ((OperationalError,ResourceClosedError))")
            session.rollback()
        except DrobloBroadException:
            logging.exception("Rolling back update_path (DrobloBroadException)")
            session.rollback()

    @staticmethod
    def delete_path(session, path: str):
        """
        Deletes paths from config (called following a on_deleted event)
        :param path:
        :param session:
        """
        if not session:
            logging.warning("No session or session is disconnected")
            return

        host = socket.gethostname()

        delete_path_stmt = delete(Paths). \
            where(Paths.host == host). \
            where(Paths.path == path). \
            where(Paths.excluded is False)
        session.execute(delete_path_stmt)

        try:
            session.commit()
        except (OperationalError, ResourceClosedError):
            logging.exception("Rolling back delete_path ((OperationalError,ResourceClosedError))")
            session.rollback()
        except DrobloBroadException:
            logging.exception("Rolling back delete_path (DrobloBroadException)")
            session.rollback()


class DrobloStatus(Base):
    """
    DrobloStatus
    Table to keep track of the different droblo processes.
    """
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String, nullable=False, unique=False)
    status = Column(String, nullable=False, unique=False)
    start_time = Column(DateTime, nullable=False, unique=False)
    update_time = Column(DateTime, nullable=True, unique=False)
    end_time = Column(DateTime, nullable=True, unique=False)
    status_index = Index("status_index", host, status, unique=True)

    def _pg_upsert(self, data):
        """
        insert or update into status
        :param data:
        """
        insert_stmt = pginsert(DrobloStatus).values(host=data["host"],
                                                    status=data["status"],
                                                    start_time=data["start_time"],
                                                    update_time=data["update_time"],
                                                    end_time=data["end_time"])
        do_update_stmt = insert_stmt.on_conflict_do_update(
            index_elements=DrobloStatus.status_index.columns,
            set_=dict(start_time=data["start_time"],
                      update_time=data["update_time"],
                      end_time=data["end_time"])
        )
        self.session.execute(do_update_stmt)
        self.session.commit()

    def _delete_and_insert(self, data):
        """
        insert or update into status
        :param data:
        """
        delete_stmt = delete(DrobloStatus). \
            where(DrobloStatus.host == data["host"]). \
            where(DrobloStatus.status == data["status"])

        insert_stmt = insert(DrobloStatus).values(host=data["host"],
                                                  status=data["status"],
                                                  start_time=data["start_time"],
                                                  update_time=data["update_time"],
                                                  end_time=data["end_time"])

        self.session.execute(delete_stmt)
        self.session.execute(insert_stmt)
        self.session.commit()

    def __init__(self, session, data=None):
        if session:
            self.session = session
        else:
            logging.warning("No session or session is disconnected")
            return
        if data:
            driver_name = get_session_driver_name(session=self.session)
            try:
                if driver_name == __PSYCOPG2__:
                    self._pg_upsert(data)
                else:
                    self._delete_and_insert(data)
            except (OperationalError, ResourceClosedError):
                logging.warning("Failed to update status on %s ((OperationalError,ResourceClosedError))" % driver_name)
                logging.warning("Rolling back")
                self.session.rollback()
            except DrobloConnectivityLostException:
                logging.warning("Failed to update status on %s (DrobloConnectivityLostException)" % driver_name)
                logging.warning("Rolling back")
                self.session.rollback()
            except DrobloBroadException:
                logging.warning("Failed to update status on %s (DrobloBroadException)" % driver_name)
                logging.warning("Rolling back")
                self.session.rollback()

    def is_clean(self, host):
        """
        Check if the watcher is already on host started before populating.
        If the watcher is not started since at least __SECONDS_THRESHOLD_FOR_CLEAN__ seconds, return false.
        This is a totally arbitrary decision. :P
        :param host:
        :return:
        """

        if self.session and self.is_watcher_running(host):
            watch_update_time = self.session.query(DrobloStatus.update_time). \
                filter(DrobloStatus.status == "watch"). \
                filter(DrobloStatus.host == host).scalar()
            populate_start_time = self.session.query(DrobloStatus.start_time). \
                filter(DrobloStatus.status == "populate"). \
                filter(DrobloStatus.host == host).scalar()
            if (populate_start_time - watch_update_time).seconds < __SECONDS_THRESHOLD_FOR_CLEAN__:
                return True
        return False

    def is_watcher_running(self, host):
        """
        Check if the watcher is running for host, by making sure the end time is not set
        :param host:
        :return:
        """

        watch_end_time = self.session.query(DrobloStatus.end_time). \
            filter(DrobloStatus.status == "watch"). \
            filter(DrobloStatus.host == host).all()

        if not len(watch_end_time):
            return False
        return False if watch_end_time else True


class DeletedFiles(Base):
    """
    files
    """
    __tablename__ = 'deleted_files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String(32), nullable=False, unique=False)
    file = Column(String, nullable=False, unique=True)


class Files(Base):
    """
    files
    """
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String(32), nullable=False, unique=False)
    file = Column(String, nullable=False, unique=True)
    hash = Column(BLOB(32), nullable=False, unique=False)
    atime = Column(DateTime, nullable=False, unique=False)
    ctime = Column(DateTime, nullable=False, unique=False)
    mtime = Column(DateTime, nullable=False, unique=False)
    size = Column(BigInteger, nullable=False, unique=False)
    file_index = Index("file_index", host, file, unique=True)
    hash_index = Index("hash_index", host, hash, unique=False)
    size_index = Index("size_index", host, size, unique=False)

    def __init__(self, session, data=None):
        self.session = session
        self.driver_name = get_session_driver_name(self.session)
        if data and self.session:
            if isinstance(data, dict):
                self._handle_data(data)
            elif isinstance(data, list):
                for d in data:
                    self._handle_data(d)

    def _handle_data(self, data):
        if "hash" in data:  # on_created, on_modified
            self._upsert(data)
        elif "moved_dir" in data:  # on_moved
            if self.driver_name == __PSYCOPG2__:
                self._regex_update(data)
            else:
                self._sqlite_update(data)
        elif "moved_file" in data:  # on_moved
            # TODO : Check why we used to have below line

            # self._delete({"host": data["host"], "deleted": data["src"]})
            if self.driver_name == __PSYCOPG2__:
                self._regex_update(data)
            else:
                self._sqlite_update(data)
        else:  # on_deleted
            self._delete(data)

    def _upsert(self, data):
        if self.driver_name == __PSYCOPG2__:
            self._pg_upsert(data)
        else:
            self._delete_and_insert(data)

    def _pg_upsert(self, data):
        """
        insert or update into files
        :param data:
        """
        try:
            insert_stmt = pginsert(Files).values(host=data["host"],
                                                 file=data["file"], hash=data["hash"],
                                                 atime=data["atime"], ctime=data["ctime"],
                                                 mtime=data["mtime"], size=data["size"]
                                                 )
            do_update_stmt = insert_stmt.on_conflict_do_update(index_elements=Files.file_index.columns,
                                                               set_=dict(hash=data["hash"],
                                                                         atime=data["atime"], ctime=data["ctime"],
                                                                         mtime=data["mtime"], size=data["size"]
                                                                         )
                                                               )

            self.session.execute(do_update_stmt)
            self.session.commit()
        except (OperationalError, ResourceClosedError):
            logging.error("Failed to upsert on %s ((OperationalError,ResourceClosedError))" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()
        except DrobloBroadException:
            logging.error("Failed to upsert on %s (DrobloBroadException)" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()

    def _delete_and_insert(self, data):
        """
        insert or update into files
        :param data:
        """
        try:
            delete_stmt = delete(Files).where(Files.host == data["host"]).where(Files.file == data["file"])

            insert_stmt = insert(Files).values(host=data["host"],
                                               file=data["file"], hash=data["hash"],
                                               atime=data["atime"], ctime=data["ctime"],
                                               mtime=data["mtime"], size=data["size"]
                                               )
            self.session.execute(delete_stmt)
            self.session.execute(insert_stmt)
            self.session.commit()
        except (OperationalError, ResourceClosedError):
            logging.error("Failed to upsert on %s ((OperationalError,ResourceClosedError))" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()
        except DrobloBroadException:
            logging.error("Failed to upsert on %s (DrobloBroadException)" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()

    def delete_from_list(self, list_files_to_delete):
        if self.session:
            for data in list_files_to_delete:
                self._delete(data=data)

    def _delete(self, data):
        """
        _delete entries from files
        :param data:
        """
        if self.driver_name != __PSYCOPG2__:
            try:
                insert_stmt = insert(DeletedFiles). \
                    values(host=data["host"], file=data["deleted"])
                self.session.execute(insert_stmt)
                self.session.commit()
            except (OperationalError, ResourceClosedError):
                logging.error("Failed to delete on %s ((OperationalError,ResourceClosedError))" % self.driver_name)
                logging.error("Rolling back.")
                self.session.rollback()
                raise DrobloConnectivityLostException()
            except DrobloBroadException:
                logging.error("Failed to delete on %s (DrobloBroadException)" % self.driver_name)
                logging.error("Rolling back.")
                self.session.rollback()
                raise DrobloConnectivityLostException()

        try:
            delete_stmt = delete(Files). \
                where(Files.host == data["host"]). \
                where(Files.file.like(data["deleted"] + "%"))
            self.session.execute(delete_stmt)
            self.session.commit()
        except (OperationalError, ResourceClosedError):
            logging.error("Failed to delete on %s ((OperationalError,ResourceClosedError))" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()
        except DrobloBroadException:
            logging.error("Failed to delete on %s (DrobloBroadException)" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()

    def _regex_update(self, data):

        """
        insert or update into files
        :param data:
        """
        try:
            regex_stmt = update(Files). \
                where(Files.host == data["host"]). \
                values(file=func.regexp_replace(Files.file, data["src"], data["dst"]))
            self.session.execute(regex_stmt)
            self.session.commit()
        except (OperationalError, ResourceClosedError):
            logging.error("Failed to update on %s ((OperationalError,ResourceClosedError))" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()
        except DrobloBroadException:
            logging.error("Failed to update on %s (DrobloBroadException)" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()

    def _sqlite_update(self, data):
        """
        insert or update into files
        :param data:
        """
        try:
            original = self.session.query(Files). \
                filter(Files.host == data["host"]). \
                filter(Files.file == data["src"]).all()[0]

            delete_stmt = delete(Files).where(Files.host == data["host"]).where(Files.file == data["src"])

            insert_stmt = insert(Files).values(host=data["host"],
                                               file=data["dst"], hash=original.hash,
                                               atime=original.atime, ctime=original.ctime,
                                               mtime=original.mtime, size=original.size
                                               )
            self.session.execute(delete_stmt)
            self.session.execute(insert_stmt)
            self.session.commit()
        except (OperationalError, ResourceClosedError):
            logging.error("Failed to update on %s ((OperationalError,ResourceClosedError))" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()
        except DrobloBroadException:
            logging.error("Failed to update on %s (DrobloBroadException)" % self.driver_name)
            logging.error("Rolling back.")
            self.session.rollback()
            raise DrobloConnectivityLostException()
