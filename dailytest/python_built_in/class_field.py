#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/7 17:55


# 内置的类属性
class BuiltInClassField(object):
    """类的内置属性"""
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        BuiltInClassField.count += 1

    def getCount(self):
        return BuiltInClassField.count

    def getPrivateField(self):
        return self.name, self.age


print "BuiltInClassField.__module__:", BuiltInClassField.__module__

if __name__ == '__main__':
    print "BuiltInClassField.__doc__:", BuiltInClassField.__doc__
    print "BuiltInClassField.__name__:", BuiltInClassField.__name__
    print "BuiltInClassField.__module__:", BuiltInClassField.__module__
    print "BuiltInClassField.__bases__:", BuiltInClassField.__bases__
    print "BuiltInClassField.__dict__:", BuiltInClassField.__dict__
