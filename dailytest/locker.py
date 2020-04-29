#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/25 15:38
import time
import sys
import traceback


class Mutex(object):
    LOCKER_OVERTIME = 3
    abstract_lock = False

    def __init__(self, key, overtime_sec=LOCKER_OVERTIME):
        self.key = key
        self.overtime = overtime_sec

    def lock(self):
        print 'this is lock function:', self.key
        self.abstract_lock = True

    def unlock(self):
        print 'this is unlock function:', self.key
        self.abstract_lock = False

    def __enter__(self):
        self.lock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # raise Exception("Too many connections")
        self.unlock()

    def lock_stat(self, location=0):
        print 'location:', location, ' abstract_lock:', self.abstract_lock


def action():
    with Mutex(key='action execute'):
        raise Exception('occur an exception')
        # print 'action execute normal'
    print '获取奖励'


def print_exc(limit=None, file=None):
    """Shorthand for 'print_exception(sys.exc_type, sys.exc_value, sys.exc_traceback, limit, file)'.
    (In fact, it uses sys.exc_info() to retrieve the same information
    in a thread-safe way.)"""
    if file is None:
        file = sys.stderr
    try:
        etype, value, tb = sys.exc_info()
        print_exception(etype, value, tb, limit, file)
    finally:
        etype = value = tb = None


def print_exception(etype, value, tb, limit=None, file=None):
    """Print exception up to 'limit' stack trace entries from 'tb' to 'file'.

    This differs from print_tb() in the following ways: (1) if
    traceback is not None, it prints a header "Traceback (most recent
    call last):"; (2) it prints the exception type and value after the
    stack trace; (3) if type is SyntaxError and value has the
    appropriate format, it prints the line where the syntax error
    occurred with a caret on the next line indicating the approximate
    position of the error.
    """
    error_str = ''
    if file is None:
        file = sys.stderr
    if tb:
        error_str = 'Traceback (most recent call last): \n'
        error_str += _return_tb_message(tb, limit=limit)

    lines = traceback.format_exception_only(etype, value)

    for line in lines:
        error_str += line + '\n'
    if error_str:
        # import logging
        # logging.error(error_str)
        print error_str


def _return_tb_message(tb, limit=None):
    """Print up to 'limit' stack trace entries from the traceback 'tb'.

    If 'limit' is omitted or None, all entries are printed.  If 'file'
    is omitted or None, the output goes to sys.stderr; otherwise
    'file' should be an open file or file-like object with a write()
    method.
    """

    if limit is None:
        if hasattr(sys, 'tracebacklimit'):
            limit = sys.tracebacklimit
    n = 0
    message = ''
    while tb is not None and (limit is None or n < limit):
        f = tb.tb_frame
        lineno = tb.tb_lineno
        co = f.f_code
        filename = co.co_filename
        name = co.co_name
        message += '  File "%s", line %d, in %s' % (filename, lineno, name) + '\n'

        traceback.linecache.checkcache(filename)
        line = traceback.linecache.getline(filename, lineno, f.f_globals)
        if line:
            message += '    ' + line.strip() + '\n'
        tb = tb.tb_next
        n = n + 1
    return message


if __name__ == '__main__':
    mutex = Mutex(key='outer sphere')
    try:
        with mutex:
            mutex.lock_stat(location=0)
            response = action()
            # mutex.lock_stat(location=1)
            # print response

        mutex.lock_stat(location=2)

    except Exception as e:
        mutex.lock_stat(location=3)
        print 'exception:', e
        print_exc(e)