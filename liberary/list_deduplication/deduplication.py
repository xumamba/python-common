#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 上午10:59
# @Author  : serendipity-xp
# @FileName: deduplication.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp


def deduplication_set(data_list):
    """
    用set进行列表去重
    :param data_list:
    :return:
    """
    return list(set(data_list))


def deduplication_groupby(data_list):
    import itertools
    data_list.sort()
    it = itertools.groupby(data_list)
    for k, g in it:
        print k


def difference_set(list1, list2):
    """
    两个列表取差集
    :param list1:
    :param list2:
    :return:
    """
    return list(set(list1) ^ set(list2))


if __name__ == '__main__':
    test_list = [300, 301, 302, 303, 304, 305, 302, 305]
    result = deduplication_set(test_list)
    print result
    deduplication_groupby(test_list)
    l = difference_set([300, 303], [300, 301, 302, 303, 304, 305])
    print l

