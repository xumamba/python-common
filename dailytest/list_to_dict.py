#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 下午3:38
# @Author  : serendipity-xp
# @FileName: list_to_dict.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp

from gunicorn.six import iteritems


def list2dict(conf):
	l = [(key, value) for key, value in iteritems(conf)
			  if key in ('key3', 'key2') and value is not None]
	print l
	d = dict(l)
	print isinstance(d, dict)
	print d


if __name__ == '__main__':
	my_conf = {'key1': 1, 'key2': 'string','key3': [123]}
	list2dict(my_conf)
