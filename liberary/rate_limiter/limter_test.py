#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 下午5:34
# @Author  : serendipity-xp
# @FileName: limter_test.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
import unittest
from liberary.rate_limiter.token_bucket import TokenBucket
from time import sleep


class TestTokenBucket(unittest.TestCase):

    def test_conusme(self):
        token_bucket = TokenBucket(6, 6)
        for x in range(15):
            permit = token_bucket.consume(1)
            if x == 6 or x == 13:
                self.assertFalse(permit)
                sleep(1)
            else:
                self.assertTrue(permit)
