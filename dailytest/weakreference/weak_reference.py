#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/13 9:40
import sys
import weakref
from dailytest.weakreference.cycle_reference import Request, demo

class Man:
    def __init__(self, name):
        self.name = name

    def test(self):
        print '{name},this is a test'.format(name=self.name)


def callback(self):
    print 'this is a callback function'


class WeakRequest(Request):
    # 使用弱引用
    def set_next(self, other):
        if other is not None:
            if self in other.all_nodes():
                other = weakref.proxy(other)
        super(Request, self).set_next(other)
        return


if __name__ == '__main__':
    obj = Man('Tom')
    print sys.getrefcount(obj)  # get the reference count of obj

    r = weakref.ref(obj)  # 创建一个弱引用
    print sys.getrefcount(obj)  # 应用计数并没有发生变化

    print 'weakref:', r  # 弱引用所指向的对象信息  <weakref at 02C6BED0; to 'instance' at 02C744E0>
    obj2 = r()  # 获取弱引用所指向的对象

    print 'obj:', obj
    print 'obj2:', obj2
    assert obj is obj2  # True

    print sys.getrefcount(obj)  # +1

    print weakref.getweakrefcount(obj)  # 返回弱引用数 1
    print weakref.getweakrefs(obj)  # 返回引用列表 [<weakref at 02C3BED0; to 'instance' at 02C444E0>]

    obj = None
    obj2 = None
    print 'r:', r  # 当对象引用计数为零时，弱引用失效。 <weakref at 02C6BED0; dead>

    man_obj = Man('Jerry')
    proxy_obj = weakref.proxy(man_obj, callback)  # 创建代理对象
    proxy_obj.test()
    man_obj = None
    proxy_obj.test()  # ReferenceError
    # demo(WeakRequest)






