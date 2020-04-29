#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/8 16:02
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, TooManyRedirects, \
    ReadTimeout, ConnectTimeout, ConnectionError, HTTPError

class HttpClientConn(object):

    _session = None

    @classmethod
    def init(cls):
        cls._session = requests.Session()
        cls._session.mount('http://', HTTPAdapter(pool_connections=16, pool_maxsize=32))

    @classmethod
    def get_conn(cls):
        if not cls._session:
            cls.init()
        return cls._session


if __name__ == '__main__':
    conn = HttpClientConn.get_conn()
    response = ''
    try:
        response = conn.request(
            method='POST',
            url='http://www.baidu.com',
            json='{data:value}',
            headers={
                'User-Agent': 'test flag',
                'Content-Type': 'application/json; charset=utf-8',  # 'application/x-www-form-urlencoded'
            },
            timeout=3
        )
    except(TooManyRedirects, ReadTimeout, ConnectTimeout, ConnectionError,
            HTTPError, RequestException) as e:
        print e
    assert response.status_code == 200
    print response.text

