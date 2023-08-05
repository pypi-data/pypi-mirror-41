# coding=utf-8
"""
Filesystem functions.
"""
from os import kill, getpid
from signal import SIGILL
import socket
import re
import time
import logging
import threading

__INITIAL_INTERVAL__ = 3
__MAX_INTERVAL_STEPS__ = 10


class DrobloPostgreSQLPoller(threading.Thread):
    """
    Thread polling our postgre server, sends a signal to droblod upon availability.
    """
    def __init__(self, connection_string, droblo_poll, sig=SIGILL, interval=__INITIAL_INTERVAL__):
        super().__init__()
        self.droblo_poll = droblo_poll
        self._steps = interval
        self._interval = interval
        self._connection_string = connection_string
        self._signal_to_send = sig
        self._server = None
        self._port = None
        self._server_reachable = True
        self._parse_connection_string()
        self._test_srv_connectivity()
        logging.info(f"DrobloPostgreSQLPoller initialized, polling {self._server}")
        logging.info(f"{self._server} is %sreacheable" % ("" if self.server_reachable else "un"))

    def run(self):
        """
        threading.Thread run override.
        """
        try:
            while self.droblo_poll.is_set():
                self._test_srv_connectivity()
                time.sleep(self.interval)
            logging.info("Exiting DrobloPostgreSQLPoller")
        except (KeyboardInterrupt, SystemExit):
            logging.info("Exiting DrobloPostgreSQLPoller")

    @property
    def interval(self) -> int:
        """
        Polling interval in seconds
        :return:
        """
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value
        logging.info("Polling for %s connectivity every %s seconds." % (self._server, self.interval))

    @property
    def server_reachable(self) -> bool:
        """
        Server is reachable boolean.
        :return:
        """
        return self._server_reachable

    @server_reachable.setter
    def server_reachable(self, value):
        if value != self._server_reachable:
            self._server_reachable = value
            self._send_reconnect_signal()

    def _parse_connection_string(self):
        match = re.search(r'postgresql://.*:.*@(?P<srv>.*):(?P<port>.*)/.*', self._connection_string)
        if match:
            self._server = match.group("srv")
            self._port = int(match.group("port"))

    def _test_srv_connectivity(self):
        s = socket.socket()
        try:
            s.connect((self._server, self._port))
            self.server_reachable = True
        except socket.error as _:
            if self.interval < __MAX_INTERVAL_STEPS__ * self._steps:
                self.interval += self._steps
            self.server_reachable = False
        finally:
            s.close()

    def _send_reconnect_signal(self):
        if self.server_reachable:
            logging.info("%s reachable." % self._server)
            logging.info("Resetting polling interval.")
            self.interval = self._steps
            kill(getpid(), self._signal_to_send)
        else:
            logging.warning("%s unreachable." % self._server)


def _acknowledge(signum, _):
    print("Received signal %s" % signum)


if __name__ == "__main__":
    from pap_logger import *
    from signal import signal

    PaPLogger(level=DEBUG)
    signal(SIGILL, _acknowledge)
    do_poll = threading.Event()
    do_poll.set()
    try:
        DrobloPostgreSQLPoller("postgresql://user:pass@postgresSQL:5432/db", droblo_poll=do_poll, interval=1).start()
        while True:
            print("hello")
            time.sleep(2)
    except KeyboardInterrupt:
        do_poll.clear()
        print("Bye!")
