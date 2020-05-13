#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/5/11 11:53
import gevent
import time
from gevent import monkey

monkey.patch_all()


def search_db(i):
    print 'task{i} begin...'.format(i=i)
    time.sleep(3)
    print 'task{i} end...'.format(i=i)


def win():
    return 'You Win!'


def fail():
    raise Exception('You failed!')


if __name__ == '__main__':
    now = time.time()
    tasks = [gevent.spawn(search_db, i) for i in range(3)]
    print tasks
    gevent.joinall(tasks, timeout=3)
    # for i in range(3):
    #     search_db(i)
    print 'elpase time:', time.time() - now

    print '-'*50

    winner = gevent.spawn(win)
    loser = gevent.spawn(fail)

    print winner.started
    print loser.started

    try:
        gevent.joinall([winner, loser])
    except Exception as e:
        print 'This will never be reached, because routine exception can not raise routine outside.'

    print winner.ready()
    print loser.ready()

    print winner.value
    print loser.value

    print winner.successful()
    print loser.successful()

    print loser.exception


