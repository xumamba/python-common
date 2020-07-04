#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xulp
# @DateTime: 2020/6/22 15:13


class PropertyTest(object):

    def __init__(self, name):
        self.name = name
        self.age = "hello"

class DALDescriptor(object):
    """
    数据服务访问管理类描述器
    """

    def __get__(self, instance, owner):
        return PropertyTest(owner.model_class, owner)


class IntergerDescriptor(object):
    def __init__(self):
        self.fun = 0

    def __set__(self, instance, value):
        if isinstance(value, int):
            self._interger = value
            return
        raise Exception("value must int")

    def __get__(self, instance, owner):
        return self.fun()


class A(object):
    age = IntergerDescriptor()
    sex = 1


if __name__ == '__main__':
    # print not []
    # print not None
    # test_boj = PropertyTest('aaa')
    # print test_boj.age
    # test_boj.age = 1
    # print test_boj.age
    # a = A()
    # a.age = 1
    # print a.age
    # a.sex = "str"
    # print a.sex

    dict_test = dict()
    dict_test.update({"event_count": {'7-5': 1}})
    print dict_test
    if 'event_count' in dict_test:
        event_count = dict_test.pop('event_count')
        print dict_test
        print event_count
        dict_test.update(event_count)
    print dict_test

