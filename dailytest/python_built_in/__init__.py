#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/7 17:54
import sys


class BaseAction(object):
    def get_int(self, value, validate=None):
        if validate and not validate(value):
            return False
        return True


def judge(x):
    return x < 5


if __name__ == '__main__':
    obj = BaseAction()
    assert not obj.get_int(5, judge)
    assert obj.get_int(4, judge)
