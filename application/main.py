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
    init_service()
    args = parse_args()
    runtime_logger.info("server is staring")
    app.run(host='0.0.0.0', port=args.port, debug=True)
