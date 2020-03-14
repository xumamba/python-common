# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 上午9:27
# @Author  : serendipity-xp
# @FileName: multi_process.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp

import os
import random
import time
from multiprocessing import Pool


def write(q):
    for value in ['A', 'B', 'C', 'D']:
        print 'put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        value = q.get()
        print 'get %s from queue...' % value


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpgid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


def create_pid():
    print 'Process (%s) start...' % os.getpid()
    child_pid = os.fork()
    if child_pid == 0:
        print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
    else:
        print 'I (%s) just created a child process (%s).' % (os.getpid(), child_pid)


if __name__ == '__main__':
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    # pw.start()
    # pr.start()
    # pw.join()
    # pr.terminate()

    # p = Pool()
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    # print 'Waiting for all processes done...'
    # p.close()
    # p.join()
    # print 'All processes done.'

    create_pid()
