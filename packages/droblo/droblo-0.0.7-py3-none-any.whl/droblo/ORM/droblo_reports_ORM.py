# coding=utf-8
"""
Reporting queries
"""
from datetime import datetime, timedelta

from sqlalchemy import func, or_
import pandas as pd

from droblo.ORM.droblo_ORM import Files, DrobloStatus


class DrobloReports:
    """
    Reporting queries returned as pandas DataFrame
    """

    def __init__(self, session):
        self.session = session
        self.con = self.session.bind.engine

    def get_list_hosts(self, as_list=False) -> [list, pd.DataFrame]:
        """

        :param as_list:
        :return:
        """
        q = self.session.query(func.distinct(Files.host).label("Hosts"))
        if as_list:
            return [h.Hosts for h in q.all()]
        else:
            return pd.read_sql(sql=q.statement, con=self.con)

    def get_duplicated_files(self, host=None, min_size=None, modified_after=None, order=True):
        """
        Returns the list of duplicated files
        :param host:
        :param min_size:
        :param modified_after:
        :return:
        """
        dup = func.count(Files.hash).label("dup")
        sub_q = self.session.query(dup, Files.hash.label("hash")). \
            group_by(Files.hash). \
            having(dup > 1).subquery()

        q = self.session.query(Files, sub_q.c.dup). \
            join(sub_q, Files.hash == sub_q.c.hash)
        if host:
            q = q.filter(Files.host == host)
        if min_size:
            q = q.filter(Files.size > min_size)
        if modified_after:
            q = q.filter(Files.mtime > modified_after)
        if order:
            q = q. \
                order_by(sub_q.c.dup.desc()). \
                order_by(Files.size.desc()). \
                order_by(Files.ctime.desc())  # we want to highlight the most recent duplication.

        return pd.read_sql(sql=q.statement, con=self.con)

    def get_potential_disk_space_savings(self, host=None):
        """
        :return
        :param host:
        :return:
        """
        df = self.get_duplicated_files(host=host)
        df = pd.DataFrame(df.groupby(by=["host"])["size"].sum())
        if host:
            return df.query("host=='%s'" % host)
        else:
            return df

    def get_inactive_watchers(self) -> pd.DataFrame:
        """

        :return:
        """
        update_time_threshold = datetime.now() + timedelta(seconds=-60)
        q = self.session.query(DrobloStatus.host,
                               DrobloStatus.start_time,
                               DrobloStatus.update_time,
                               DrobloStatus.end_time). \
            filter(DrobloStatus.status == "watch"). \
            filter(or_(~DrobloStatus.end_time.is_(None), DrobloStatus.update_time < update_time_threshold))
        return pd.read_sql(sql=q.statement, con=self.con)
