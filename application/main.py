#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 上午11:17
# @Author  : serendipity-xp
# @FileName: main.py.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
"""
simple web application
"""
from flask import Flask, request
import argparse
import logging
from liberary.json_utils import json_utils as json
from application.service import Service, Request


app = Flask(__name__)
runtime_logger = logging.Logger('runtime logger')


@app.route('/', methods=('GET', 'POST'))
def index():
    return '<h1>Hello python web application with flask!</h1>'


@app.route('/user/<name>', methods=('GET', 'POST'))
def user(name):
    return '<h1>Hello,%s!</h1>' % name


@app.route('/test', methods=('GET', 'POST'))
def daily_test():
    assert request.is_json
    req_args = request.get_json()
    assert isinstance(req_args, dict)

    for k, v in req_args.iteritems():
        print k, ':', v
        print type(v)
    request_args = {(k.lower() if isinstance(k, basestring) else k): v for k, v in req_args.iteritems()}
    loads = json.loads(request_args['info'], encoding="utf-8")
    print loads
    assert isinstance(loads, dict)
    return json.dumps(req_args)


@app.route('/action', methods=('GET', 'POST'))
def action():
    ip = request.remote_addr
    request_args = request.get_json()
    request_args["ip"] = ip
    response = Service.execute_action(request_args)
    return json.dumps(response)


def parse_args():
    parser = argparse.ArgumentParser(description='Server start argument')
    parser.add_argument('--port', help='Server Listen http port', type=int, default=8080)
    return parser.parse_args()


def init_service():
    runtime_logger.setLevel(logging.INFO)
    # formatter = logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # runtime_logger.setFormatter(formatter)


if __name__ == '__main__':
    # d = dict({1: [1, 3, 4], 2: [4, 5]})
    # json.loads(d)

    print "code: %d\ninfo: %s" % (101, 'info')
    s = [0,1,2,3,4,5,6,7,8,9,10]
    print s[0:9]
    init_service()
    args = parse_args()
    runtime_logger.info("server is staring")
    app.run(host='0.0.0.0', port=args.port, debug=True)

# def get_json(key):
#     try:
#
#         if need_dict and not isinstance(json_data, dict):
#             json_data = dict(json_data)
#         if validate and not validate(json_data):
#             return False
#         setattr(self, key, json_data)
#         self.action_parse_args[key] = json_data
#         return self.has_param(key)
#     except (TypeError, ValueError):
#         return False
