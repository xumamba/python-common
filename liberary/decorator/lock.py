#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/10 16:39
import threading


class ObjLock(object):
    """
    对象锁
    """
    local = threading.local()
    @staticmethod
    def lock(obj_id, overtime_sec=3, try_lock_timeout=None):
        if obj_id is None:
            return
        lock_key = 'obj_lock:{ObjID}'.format(ObjID=obj_id)

        if lock_key in ObjLock.local.__dict__:
            need_lock = False


        return