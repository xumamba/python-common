#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/5/20 9:31
import functools


def print_info(info):
    def decorator(func):
        @functools.wraps(func)
        def pack(*args, **kwargs):
            print info
            return func(*args, **kwargs)
        return pack
    return decorator


class Bar(object):

    @print_info('__new__')
    def __new__(cls, *args, **kwargs):
        self = super(Bar, cls).__new__(cls)
        return self

    @print_info('__init__')
    def __init__(self, *args):
        self.name = args[0]

    @print_info('__call__')
    def __call__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    bar = Bar('test_name')
    print bar.name
    bar()

