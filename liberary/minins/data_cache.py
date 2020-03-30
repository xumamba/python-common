#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 上午10:35
# @Author  : serendipity-xp
# @FileName: data_cache.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp


class DataCacheMixin(object):
    def set_attr(self, key, value):
        setattr(self, key, value)

    def get_attr(self, key):
        return getattr(self, key, None)

    def incr_attr(self, key, increment):
        value = self.get_attr(key)
        value += increment
        self.set_attr(key, value)
        return value