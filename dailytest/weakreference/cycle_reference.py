#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/13 10:27
import weakref
import gc
from pprint import pprint


class Request(object):
    def __init__(self, args):
        self.args = args
        self.ctx = None

    def set_next(self, other):
        print '%s.set_next(%r)' % (self.args, other)
        self.ctx = other

    def all_nodes(self):
        yield self
        n = self.ctx
        while n and n.args != self.args:
            yield n
            n = n.ctx
        if n is self:
            yield n
        return

    def __str__(self):
        return '-->'.join(n.args for n in self.all_nodes())

    def __repr__(self):
        return '<%s at 0x%x args=%s' % (self.__class__.__name__, id(self), self.args)

    def __del__(self):
        print '(Deleting %s)' % self.args


def collect_and_show_garbage():
    print '\ngarbage collecting...'
    n = gc.collect()  # 收集垃圾
    print 'unreachable objects:', n
    print 'garbage list:',  gc.garbage  # 获取垃圾列表


def demo(request_factory):
    print '----------create request----------'
    one = request_factory('One')
    two = request_factory('Two')
    three = request_factory('Three')

    one.set_next(two)
    two.set_next(three)
    three.set_next(one)

    print 'one_obj:', str(one)
    collect_and_show_garbage()

    three = None
    two = None
    print '\nAfter 2 references removed'
    print str(one)
    collect_and_show_garbage()

    one = None
    print '\nremoving last reference'
    collect_and_show_garbage()


gc.set_debug(gc.DEBUG_LEAK)  # 打印无法看到的对象信息
print 'set up cycle reference\n'
demo(Request)
print '\n-----breaking the cycle and cleaning up garbage-----\n'
gc.garbage[0].set_next(None)
while gc.garbage:
    del gc.garbage[0]
print collect_and_show_garbage()