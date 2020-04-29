#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/7 17:03
import json
from datetime import datetime, date

S_ARG = 'separators'
S_TUP = (',', ':')


class MyJsonEncoder(json.JSONEncoder):
    """
    自定义JSON编码类
    """
    def default(self, o):
        if isinstance(o, datetime):
            encode_obj = o.replace(microsecond=0).__str__()
        elif isinstance(o, date):
            encode_obj = o.__str__()
        else:
            encode_obj = json.JSONEncoder.default(self, o)

        return encode_obj


def dumps(*args, **kwargs):
    # 压缩空格
    if S_ARG not in kwargs:
        kwargs[S_ARG] = S_TUP
    return json.dumps(*args, cls=MyJsonEncoder, **kwargs)


def loads(*args, **kwargs):
    return json.loads(*args, **kwargs)


__all__ = ['dumps', 'loads']


if __name__ == '__main__':

    d = {
        'a': 1,
        3: 'sdfj dlfjd',
        'now': datetime.now()
    }

    print dumps(d)
    print dumps(d, separators=(',', ':'))
