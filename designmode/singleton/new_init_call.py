#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/6/17 9:03
from designmode.singleton.singleton_test import Singleton


class A(object):
    __metaclass__ = Singleton

    def __init__(self):
        print '__init__'
        super(A, self).__init__()

    def __new__(cls, *args, **kwargs):
        print '__new__'
        return super(A, cls).__new__(cls)

    def __call__(self, *args, **kwargs):
        print '__call__'


class BaseController(object):
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = object.__new__(cls, *args, **kwargs)
        return cls._singleton


class Counter(object):
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@Counter
def foo():
    pass


if __name__ == '__main__':
    print dir(A)
    print 'a1:', A()
    # print A().instance




    # for i in range(111):
    #     foo()
    #
    # print foo.count
