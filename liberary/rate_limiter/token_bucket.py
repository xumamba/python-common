# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 下午9:01
# @Author  : serendipity-xp
# @FileName: token_bucket.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
from time import time, sleep
from threading import RLock


class TokenBucket(object):
    def __init__(self, capacity, rate):
        self._capacity = capacity
        self._tokens = capacity
        self._rate = rate
        self._lock = RLock()
        self._latest_time = time()

    def _current_tokens(self):
        with self._lock:
            if self._tokens < self._capacity:
                now = time()
                growth = (now - self._latest_time) * self._rate
                self._tokens = min(self._tokens + growth, self._capacity)
                self._latest_time = now
            return self._tokens

    def consume(self, tokens):
        with self._lock:
            if tokens <= self._current_tokens():
                self._tokens -= tokens
                return True
            return False


if __name__ == '__main__':
    token_bucket = TokenBucket(6, 6)
    for x in range(15):
        if token_bucket.consume(2):
            print 'pid:%d, execute successful at %s' % (x, time())
        else:
            sleep(1)
            print 'pid:%d, execute failed at %s' % (x, time())
