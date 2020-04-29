#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/28 13:49
from Queue import Queue


queue = Queue(0)


def print_qsize(id=1):
    print '{id}:{size}'.format(id=id, size=queue.qsize())


if __name__ == '__main__':
    print_qsize()
    queue.put('hello')
    print_qsize(2)
    queue.put('world')
    print_qsize(3)
    task = queue.get()
    print_qsize(4)
    print task
    del task
    print_qsize(5)
