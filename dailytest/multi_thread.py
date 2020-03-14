# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 上午11:22
# @Author  : serendipity-xp
# @FileName: multi_thread.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
import time
import threading

local_obj = threading.local()


def process_single_obj():
    print 'Hello, %s (in %s)' % (local_obj.single, threading.current_thread().name)


def process_thread(name):
    local_obj.single = name
    process_single_obj()


def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


if __name__ == '__main__':
    print 'thread %s is running...' % threading.current_thread().name
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print 'thread %s ended.' % threading.current_thread().name