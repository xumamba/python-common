#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/7 15:04
from application.service import action_register


@action_register(action_id=101)
class SayHello(object):
    def __init__(self, request_args):
        self.args = request_args

    def before(self):
        print 'Performs prior logical processing'
        return True

    def execute(self):
        print 'Business logic execution'
        return True

    def after(self):
        print 'After the business logic is executed'
        return True
