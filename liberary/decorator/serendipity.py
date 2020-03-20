#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 下午4:37
# @Author  : serendipity-xp
# @FileName: serendipity.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
import logging
import functools


def err_handle(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(e.message)
    return wrapper


def err_handle_with_return(info=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(e.message)
                return info
        return wrapper
    return decorator


if __name__ == '__main__':
    class TestDecorator(object):
        @err_handle
        def test_err_handle(self):
            raise StandardError('test_err_handle')

        @err_handle_with_return(info='i can handing errors')
        def test_err_handle_with_return(self):
            raise StandardError('test_err_handle_with_return')

    @err_handle
    def comm_func1():
        raise StandardError('comm_func1')

    @err_handle_with_return(info='my name is comm_func2')
    def comm_func2():
        pass

    print 'comm_func1:', comm_func1()
    print 'comm_func2:', comm_func2()
    test_decorator = TestDecorator()
    print 'test_err_handle:', test_decorator.test_err_handle()
    print 'test_err_handle_with_return:', test_decorator.test_err_handle_with_return()
