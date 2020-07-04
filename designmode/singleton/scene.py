#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/6/17 11:08


class Singleton(type):
    """Singleton Metaclass"""

    # def __new__(mcs, *args, **kwargs):
    #     print 'Singleton new...'
    #     return mcs

    def __init__(cls, name, bases, dic):
        print 'Singleton init...', name, bases, dic
        super(Singleton, cls).__init__(name, bases, dic)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        print 'Singleton call...', args, kwargs
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class BaseComponent(object):
    __metaclass__ = Singleton

    def __new__(cls, *args, **kwargs):
        print 'BaseComponent new...'
        return cls

    def __init__(self, cc_obj):
        print 'BaseComponent init...'
        self.cc = cc_obj


class HelloComponent(BaseComponent):

    # def __new__(cls, *args, **kwargs):
    #     print 'HelloComponent new...'
    #
    # def __init__(self):
    #     print 'HelloComponent init...'

    def hello(self):
        print self.cc,


class ComponentCenter(object):
    __metaclass__ = Singleton

    def __new__(cls, *args, **kwargs):
        print 'Component new...'

    def __init__(self):
        print 'ComponentCenter init...'
        self.hello = HelloComponent(self)


if __name__ == '__main__':
    print HelloComponent()
    print HelloComponent()

    print 'str_{test}'.format(test=1)


