# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 下午9:37
# @Author  : serendipity-xp
# @FileName: marshal_unmarshal.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp


import unittest

try:
    import cPickle as pickle
except ImportError:
    import pickle


class TestMarshal(unittest.TestCase):
    def test_marshal(self):
        d = dict(name='Bob', age=20, score=88)
        dump = pickle.dumps(d)
        print(dump)