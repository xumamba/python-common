#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/16 15:26
import sys
import traceback


def print_exec(limit=None):
    error_info = ''
    try:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        if exc_traceback:
            if limit is None:
                if hasattr(sys, 'tracebacklimit'):
                    limit = sys.tracebacklimit
            flag = 0
            while exc_traceback and (not limit or flag < limit):
                f = exc_traceback.tb_frame
                lineno = exc_traceback.tb_lineno
                co = f.f_code
                filename = co.co_filename
                name = co.co_name
                error_info += '  File "%s", line %d, in %s' % (filename, lineno, name) + '\n'

                traceback.linecache.checkcache(filename)
                line = traceback.linecache.getline(filename, lineno, f.f_globals)
                if line:
                    error_info += '    ' + line.strip() + '\n'
                exc_traceback = exc_traceback.tb_next
                flag = flag + 1
        lines = traceback.format_exception_only(exc_type, exc_value)
        for line in lines:
            error_info += line + '\n'
        if error_info:
            import logging
            logging.error(error_info)
    finally:
        exc_type, exc_value, exc_traceback = None

if __name__ == '__main__':
    print_exec()
