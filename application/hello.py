#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 上午11:17
# @Author  : serendipity-xp
# @FileName: hello.py.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
"""
simple web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello python web application with flask!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' % name


if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)
