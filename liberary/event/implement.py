#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 13:52
"""
事件接口实现
"""
import attr
from zope.interface import implementer
from liberary.event.interface import IActionExecute


@attr.s
class Event(object):
    """事件"""
    context = attr.ib({})


@implementer(IActionExecute)
@attr.s
class ActionExecute(Event):
    """行为执行"""
    act_id = attr.ib(None)
    description = attr.ib(None)