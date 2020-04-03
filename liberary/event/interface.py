#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 12:02
"""
事件接口定义
"""

from zope.interface import Interface, Attribute


class IEvent(Interface):
    context = Attribute('事件上下文环境')


class IActionExecute(IEvent):
    """行为执行"""
    act_id = Attribute('行为标识')
    description = Attribute('行为描述')
