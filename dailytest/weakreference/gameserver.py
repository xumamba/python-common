#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/5/18 17:57
import weakref
import sys
import gc
from pprint import pprint


class Response(object):
    def __init__(self, stat=True, info=''):
        self.stat = stat
        self.info = info

    def set_stat(self, stat):
        self.stat = stat

    def set_info(self, info):
        self.info = info


class Request(object):

    def __init__(self, request_args):
        self.args = request_args
        self.ctx = None

    def get_attribute(self, attr_name, default=None):
        return self.args.get(attr_name, default)

    def set_attribute(self, attr_name, val):
        self.args[attr_name] = val

    @property
    def action_id(self):
        action_id = self.get_attribute('actionid')
        return 0 if action_id is None else int(action_id)

    def __str__(self):
        return "->".join(n.name for n in self.ctx.request)

    def __del__(self):
        print "(Deleting %r)" % self


class ActionContext(object):

    def __init__(self, action_id):
        self.action_id = action_id
        self.request = None
        self.response = None

    @classmethod
    def create_by_request_response(cls, request, response):
        ctx = ActionContext(action_id=110)
        ctx.request = weakref.proxy(request)
        ctx.response = response
        return ctx


def pre_process(request, response):
    ctx = ActionContext.create_by_request_response(request, response)
    request.ctx = ctx


def collect_and_show_garbage():
    print "Collecting..."
    print "unreachable objects:", gc.collect()  # 收集垃圾
    print "garbage:", gc.garbage  # gc.garbage 获取垃圾列表


if __name__ == '__main__':
    req_args = {'action_id': 222, 'data': 'test'}
    response = Response()
    request = Request(req_args)
    pre_process(request, response)

    print 'request引用计数器的值：', sys.getrefcount(request)
    print 'request弱引用数量：', weakref.getweakrefcount(request), 'request弱引用列表:', weakref.getweakrefs(request)
    # 原始：
    # request引用计数器的值： 3
    # request弱引用数量： 0 request弱引用列表: []
    # weakref.proxy():
    # request引用计数器的值： 2
    # request弱引用数量： 1 request弱引用列表: [<weakproxy at 02C0BB40 to Request at 02C1B090>]

    # request.ctx.request = None
    collect_and_show_garbage()




    #
    # print 'request:', request
    # print 'refcount:', sys.getrefcount(request)
    # print 'weakrefcount:', weakref.getweakrefcount(request), 'refs:', weakref.getweakrefs(request)
    #
    # print 'request.ctx.request:', request.ctx.request
    #
    # request.set_attribute('actionid', 10001)
    #
    # weakref_obj = request.ctx.request
    # print request is weakref_obj
    #
    #
    # action_id = weakref_obj.action_id
    # print action_id

    # gc.set_debug(gc.DEBUG_LEAK)  # 打印无法看到的对象信息
