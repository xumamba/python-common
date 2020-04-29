# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 上午11:22
# @Author  : serendipity-xp
# @FileName: multi_thread.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
import time
import thread
from Queue import Queue
import threading
import logging

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


class ThreadPool(object):

    def __init__(self, maxthreads=1, name=None):
        self.task_queue = Queue(0)
        self.worker_num = 0
        self.max = maxthreads
        self.name = name or id(self)
        self.works = []

    def start(self):
        while self.worker_num < self.max:
            self._start_worker()

    def stop(self):
        while self.worker_num:
            self.task_queue.put(None)
            self.worker_num -= 1
        print('thread_pool: {name} is stop.'.format(name=self.name))

    def _start_worker(self):
        self.worker_num += 1
        curr_thread_flag = 'PoolThread-{poll_name}_{tid}'.format(poll_name=self.name, tid=self.worker_num)
        child_thread = threading.Thread(target=self._execute, name=curr_thread_flag)
        child_thread.start()
        self.works.append(child_thread)

    def _execute(self):
        # time.sleep(1)
        cur_thread = threading.currentThread()
        cur_thread_name = cur_thread.getName()
        print('WorkerThread {name} start wait task.\n'.format(name=cur_thread_name))
        task = self.task_queue.get()
        print 'received a task: {task}'.format(task=task)
        while task:
            print('current task:{task} start execute'.format(task=task))
            task()
            print 'QSize:', self.task_queue.qsize()
            # del task

    def add_task(self, task):
        self.task_queue.put(task)

        print '\nthreadpool:{name} current task queue size is:{size}'.format(name=self.name,size=self.task_queue.qsize())


pool = ThreadPool(name='test_threadpool')
pool.start()

if __name__ == '__main__':
    def task():
        time.sleep(1)
    pool.add_task(task)

    # for i in range(20):
    #     pool.add_task(lambda: time.sleep(1))




    # print 'thread %s is running...' % threading.current_thread().name
    # t = threading.Thread(target=loop, name='LoopThread')
    # t.start()
    # t.join()
    # print 'thread %s ended.' % threading.current_thread().name

    # print '---------thread.start_new_thread-----------\n'
    # try:
    #     # thread.start_new_thread(loop, ())
    #     raise ValueError
    # except Exception as e:
    #     from liberary.runtime_utils.exec_trace import print_exec
    #     print_exec(e)



