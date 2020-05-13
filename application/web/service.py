#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/7 15:05


def action_register(action_id):
    def decorator(cls):
        cls.action_id = action_id
        Service.register_action(action_id=action_id, action=cls)
    return decorator


class Service(object):
    _mapping = {}

    @classmethod
    def register_action(cls, action_id, action):
        if cls._mapping.has_key(action_id):
            raise ValueError('ActionID [%d] already exist.' % action_id)
        cls._mapping[action_id] = action

    @classmethod
    def get_action(cls, action_id):
        print cls._mapping
        return cls._mapping[action_id]

    @classmethod
    def execute_action(cls, request_args, response=None):
        request = Request(request_args)
        action = cls.get_action(request.action_id)
        action_obj = action(request.args)
        action_obj.before()
        action_obj.execute()
        action_obj.after()
        return request.args.get("ip")


class Request(object):
    def __init__(self, request_args):
        self.args = request_args
        self.ctx = None

    def get_args(self, key, default=None):
        return self.args.get(key, default)

    @property
    def action_id(self):
        return self.get_args('action_id', 0)


class Response(object):
    def __init__(self, dic):
        self.response = dic

    def serialize(self):
        import copy
        result_dict = copy.deepcopy(self.response)
        return json.dumps(result_dict)
