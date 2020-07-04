#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xulp
# @DateTime: 2020/5/22 14:56
from time import time, sleep


class Singleton(type):
    """Singleton Metaclass"""

    def __init__(cls, name, bases, dic):
        print 'Singleton__init__'
        super(Singleton, cls).__init__(name, bases, dic)
        cls.instance = None

    # def __call__(cls, *args, **kwargs):
    #     print 'cls:', cls
    #     print 'Singleton__call__'
    #     if cls.instance is None:
    #         cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
    #     return cls.instance


# class MyClass(object):
#
#     __metaclass__ = Singleton
#
#     default_lang = 'zh-cn'
#
#     @classmethod
#     def class_func(cls):
#         print cls.default_lang


if __name__ == '__main__':
    # my_class1 = MyClass()
    # my_class2 = MyClass()
    # assert id(my_class1) == id(my_class2)
    # setattr(my_class2, 'key', None)
    # print hasattr(my_class2, 'key')
    # print getattr(my_class2, 'key')

    attrs = ((('prefix_'+name, value) for name, value in {'one': 1, 'two': True}))
    print type(attrs), attrs
    _attrs = dict((name, value) for name, value in attrs)
    print _attrs