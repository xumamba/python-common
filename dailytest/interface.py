#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 上午9:38
# @Author  : serendipity-xp
# @FileName: interface.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp

from zope.interface import Interface
from zope.interface.declarations import implementer


# 定义接口
class Miss(Interface):
    def i_miss_you(self, miss):
        """Say i miss you"""


# 实现接口
@implementer(Miss)
class MyMiss:
    def __init__(self):
        pass

    def i_miss_you(self, name):
        return 'I miss you %s' % name


if __name__ == '__main__':
    obj = MyMiss()
    result = obj.i_miss_you('p')
    print result
