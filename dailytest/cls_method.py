#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/7 12:00


class Interceptor(object):
    middleware = []

    def __int__(self):
        self.cur_index = 0

    @classmethod
    def add_middleware(cls, middleware):
        cls.middleware.append(middleware)
        return cls

    def apply_middleware(self):
        print self.middleware


if __name__ == '__main__':
    Interceptor.add_middleware("one")
    interceptor_obj = Interceptor()
    interceptor_obj.apply_middleware()
    Interceptor.add_middleware("two")
    interceptor_obj.apply_middleware()
