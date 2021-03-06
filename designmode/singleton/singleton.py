#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/4/2 14:46


class Singleton(type):
    """Singleton Metaclass"""

    def __init__(cls, name, bases, dic):
        print 'Singleton init'
        super(Singleton, cls).__init__(name, bases, dic)

    def __new__(mcs, name, bases, dic):
        print 'Singleton new'
        return type.__new__(mcs, name, bases, dic)

    def __call__(cls, *args, **kwargs):
        print 'Singleton call'
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class InstanceFactory(object):
    __metaclass__ = Singleton

    def __new__(cls, *args, **kwargs):
        print 'instance object new', args, kwargs
        return object.__new__(cls)

    def __init__(self, *args, **kwargs):
        print 'instance object init', args, kwargs

    def __call__(self, *args, **kwargs):
        print 'instance object call'


def funcName(s):
    print '---->', s.name
    print "---->func execute"

# Singleton init
# Singleton call
# instance object new
# instance object init
# <__main__.InstanceFactory object at 0x02C28210>
# Singleton call
# <__main__.InstanceFactory object at 0x02C28210>
if __name__ == '__main__':
    t = type("InstanceFactory1", (object,), {'name': 'hello', 'funcName': funcName})
    print 'class:', t
    t_obj = t()
    print t_obj.name
    print callable(t_obj.funcName)
    print t_obj.funcName()
