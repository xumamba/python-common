# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 下午5:29
# @Author  : serendipity-xp
# @FileName: decorator.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp

import functools


def print_log(msg):
    def decorator(func):
        @functools.wraps(func)
        def pack(*args, **kw):
            print 'begin:%s %s()' % (msg, func.__name__)
            temp = func(*args, **kw)
            print 'end:%s' % func.func_code
            return temp
        return pack
    return decorator


@print_log('message')
def f(field='default'):
    print '%s execute' % f.__name__
    print f.func_code.co_varnames


if __name__ == '__main__':
    f('field')
