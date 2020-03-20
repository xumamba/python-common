#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 上午11:11
# @Author  : serendipity-xp
# @FileName: list_merge.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp


def extend_merge(list1, list2):
    return list1.extend(list2)


def add_merge(list1, list2):
    return list1 + list2


if __name__ == '__main__':
    test_l1 = [300, 303]
    test_l2 = [300, 301, 302, 303, 304, 305]
    # result = extend_merge(test_l1, test_l2)
    # print result
    result = add_merge(test_l1, test_l2)
    print result
