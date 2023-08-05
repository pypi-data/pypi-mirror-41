# -*- coding: utf-8 -*-

__author__ = 'Grzegorz Latuszek, Marcin Usielski, Michal Ernst'
__copyright__ = 'Copyright (C) 2018-2019 Nokia'
__email__ = 'grzegorz.latuszek@nokia.com, marcin.usielski@nokia.com, michal.ernst@nokia.com'

import logging
import time
from abc import abstractmethod, ABCMeta

from six import add_metaclass

from moler.exceptions import ConnectionObserverNotStarted
from moler.exceptions import ConnectionObserverTimeout
from moler.exceptions import NoConnectionProvided
from moler.exceptions import NoResultSinceCancelCalled
from moler.exceptions import ResultAlreadySet
from moler.exceptions import ResultNotAvailableYet
from moler.helpers import ClassProperty
from moler.helpers import camel_case_to_lower_case_underscore
from moler.helpers import instance_id
from moler.helpers import copy_list
from moler.runner import ThreadPoolExecutorRunner
import threading


@add_metaclass(ABCMeta)
class ConnectionObserver(object):
    _not_raised_exceptions = list()  # list of dict: "exception" and "time"
    _exceptions_lock = threading.Lock()

    def __init__(self, connection=None, runner=None):
        """
        Create instance of ConnectionObserver class
        :param connection: connection used to receive data awaited for
        """
        self.connection = connection
        self._is_running = False
        self._is_done = False
        self._is_cancelled = False
        self._result = None
        self._exception = None
        self.runner = runner if runner else ThreadPoolExecutorRunner()
        self._future = None
        self._is_command = None
        self.timeout = 7
        self.start_time = -1
        self.device_logger = logging.getLogger('moler.{}'.format(self.get_logger_name()))
        self.logger = logging.getLogger('moler.connection.{}'.format(self.get_logger_name()))

    def __str__(self):
        return '{}(id:{})'.format(self.__class__.__name__, instance_id(self))

    def __repr__(self):
        cmd_str = self.__str__()
        connection_str = '<NO CONNECTION>'
        if self.connection:
            connection_str = repr(self.connection)
        return '{}, using {})'.format(cmd_str[:-1], connection_str)

    def __call__(self, timeout=None, *args, **kwargs):
        """
        Run connection-observer in foreground
        till it is done or timeouted
        """
        if timeout:
            self.timeout = timeout
        started_observer = self.start(timeout, *args, **kwargs)
        if started_observer:
            return started_observer.await_done(*args, **kwargs)
        # TODO: raise ConnectionObserverFailedToStart

    def get_logger_name(self):
        if self.connection and hasattr(self.connection, "name"):
            return self.connection.name
        else:
            return self.__class__.__name__

    def start(self, timeout=None, *args, **kwargs):
        """Start background execution of connection-observer."""
        if timeout:
            self.timeout = timeout
        self._validate_start(*args, **kwargs)
        self._is_running = True
        self.start_time = time.time()
        self._future = self.runner.submit(self)
        if self._future is None:
            self._is_running = False
        return self

    def _validate_start(self, *args, **kwargs):
        # check base class invariants first
        if not self.connection:
            # only if we have connection we can expect some data on it
            # at the latest "just before start" we need connection
            raise NoConnectionProvided(self)
        # ----------------------------------------------------------------------
        # We intentionally do not check if connection is open here.
        # In such case net result anyway will be failed/timeouted observer -
        # - so, user will need to investigate "why".
        # Checking connection state would benefit in early detection of:
        # "error condition - no chance to succeed since connection is closed".
        # However, drawback is a requirement on connection to have is_open() API
        # We choose minimalistic dependency over better troubleshooting support.
        # ----------------------------------------------------------------------
        if self.timeout <= 0.0:
            raise ConnectionObserverTimeout(self, self.timeout, "before run", "timeout is not positive value")

    def await_done(self, timeout=None):
        """Await completion of connection-observer."""
        if self.done():
            return self.result()
        if self._future is None:
            raise ConnectionObserverNotStarted(self)
        self.runner.wait_for(connection_observer=self, connection_observer_future=self._future,
                             timeout=timeout)
        return self.result()

    def cancel(self):
        """Cancel execution of connection-observer."""
        if self.cancelled() or self.done():
            return False
        self._is_done = True
        self._is_cancelled = True
        return True

    def cancelled(self):
        """Return True if the connection-observer has been cancelled."""
        return self._is_cancelled

    def running(self):
        """Return True if the connection-observer is currently executing."""
        if self.done() and self._is_running:
            self._is_running = False
        return self._is_running

    def done(self):
        """Return True if the connection-observer is already done."""
        return self._is_done

    def set_result(self, result):
        """Should be used to set final result"""
        if self.done():
            raise ResultAlreadySet(self)
        self._is_done = True
        self._result = result

    @abstractmethod
    def data_received(self, data):
        """
        Entry point where feeders pass data read from connection
        Here we perform data parsing to conclude in result setting
        """
        pass

    def set_exception(self, exception):
        """Should be used to indicate some failure during observation"""
        if self._is_done:
            self._log(logging.WARNING,
                      "Set exception with object '{}.{}' ({}) on already done object ({}).".format(
                          exception.__class__.__module__,
                          exception.__class__.__name__,
                          exception,
                          self
                      ))
            return
        self._is_done = True
        ConnectionObserver._change_unraised_exception(new_exception=exception, observer=self)
        self._log(logging.INFO, "'{}.{}' has set exception '{}.{}' ({}).".format(self.__class__.__module__,
                                                                                 self.__class__.__name__,
                                                                                 exception.__class__.__module__,
                                                                                 exception.__class__.__name__,
                                                                                 exception))

    def result(self):
        """Retrieve final result of connection-observer"""
        with ConnectionObserver._exceptions_lock:
            ConnectionObserver._log_unraised_exceptions(self)
            if self._exception:
                exception = self._exception
                if exception in ConnectionObserver._not_raised_exceptions:
                    ConnectionObserver._not_raised_exceptions.remove(exception)
                raise exception
        if self.cancelled():
            raise NoResultSinceCancelCalled(self)
        if not self.done():
            raise ResultNotAvailableYet(self)
        return self._result

    def on_timeout(self):
        """ It's callback called by framework just before raise exception for Timeout """
        pass

    def add_command_to_connection(self, do_no_wait):
        """
        Adds blocking ConnectionObserver object (command object) to connection. If ConnectionObserver object is not
         blocking then immediately returns True.
        :param do_no_wait: If True then returns immediately from method, if False then wait till the connection is available
        to execute another command or timeout occurred.
        :return: True if ConnectionObserver was added to connection or adding is not required. False if cannot add ConnectionObserver
         to connection
        """
        return True

    def remove_command_from_connection(self):
        """
        Remove blocking ConnectionObserver object (command object) from connection. If Connection observer is not blocking
         then does nothing.
        :return: Nothing
        """
        pass

    def is_command(self):
        """
        :return: True if instance of ConnectionObserver is a command. False if not a command.
        """
        if self._is_command is None:
            self._is_command = hasattr(self, "command_string")
        return self._is_command

    def extend_timeout(self, timedelta):
        prev_timeout = self.timeout
        self.timeout = self.timeout + timedelta
        msg = "Extended timeout from %.2f with delta %.2f to %.2f" % (prev_timeout, timedelta, self.timeout)
        self.runner.timeout_change(timedelta)
        self._log(logging.INFO, msg)

    @ClassProperty
    def observer_name(cls):
        name = camel_case_to_lower_case_underscore(cls.__name__)
        return name

    @staticmethod
    def get_unraised_exceptions(remove=True):
        with ConnectionObserver._exceptions_lock:
            if remove:
                list_of_exceptions = ConnectionObserver._not_raised_exceptions
                ConnectionObserver._not_raised_exceptions = list()
                return list_of_exceptions
            else:
                list_of_exceptions = copy_list(ConnectionObserver._not_raised_exceptions)
                return list_of_exceptions

    @staticmethod
    def _change_unraised_exception(new_exception, observer):
        with ConnectionObserver._exceptions_lock:
            old_exception = observer._exception
            ConnectionObserver._log_unraised_exceptions(observer)
            if old_exception:
                observer._log(logging.DEBUG,
                              "'{}.{}' has overwritten exception. From '{}.{}' ({}) to '{}.{}' ({}).".format(
                                  observer.__class__.__module__,
                                  observer.__class__.__name__,
                                  old_exception.__class__.__module__,
                                  old_exception.__class__.__name__,
                                  old_exception,
                                  new_exception.__class__.__module__,
                                  new_exception.__class__.__name__,
                                  new_exception,
                              ))
                if old_exception in ConnectionObserver._not_raised_exceptions:
                    ConnectionObserver._not_raised_exceptions.remove(old_exception)
                else:
                    observer._log(logging.DEBUG,
                                  "'{}.{}': cannot find exception '{}.{}' '{}' in _not_raised_exceptions.".format(
                                      observer.__class__.__module__,
                                      observer.__class__.__name__,
                                      old_exception.__class__.__module__,
                                      old_exception.__class__.__name__,
                                      old_exception,
                                  ))
                    ConnectionObserver._log_unraised_exceptions(observer)

            ConnectionObserver._not_raised_exceptions.append(new_exception)
            observer._exception = new_exception

    @staticmethod
    def _log_unraised_exceptions(observer):
        observer._log(logging.DEBUG, "list length: {}".format(len(ConnectionObserver._not_raised_exceptions)))
        observer._log(logging.DEBUG, "list: {}".format(ConnectionObserver._not_raised_exceptions))

        for i, item in enumerate(ConnectionObserver._not_raised_exceptions):
            observer._log(logging.DEBUG, "{}: {}".format(i, item))

    def get_long_desc(self):
        return "Observer '{}.{}'".format(self.__class__.__module__, self.__class__.__name__)

    def get_short_desc(self):
        return "Observer '{}.{}'".format(self.__class__.__module__, self.__class__.__name__)

    def _log(self, lvl, msg, extra=None):
        extra_params = {
            'log_name': self.get_logger_name()
        }

        if extra:
            extra_params.update(extra)

        self.logger.log(lvl, msg, extra=extra_params)
        self.device_logger.log(lvl, msg, extra=extra_params)
