#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/5/19 10:20
from copy import copy, deepcopy
import json

def recharge_or_gift(product_id):
    """
    根据产品id区别产品类型(充值:能转成整型， 礼包:不能转成整型)
    :param product_id: str 产品的id
    :return:
    """
    try:
        int(product_id)
        res = "222"
        return res
    except:
        res = "444"
    finally:
        res = "333"
    print 'aaa:', res


class GameTest(object):

    def __init__(self):
        setattr(self, "one", 1)


def add_content(outer_dict):
    outer_dict['inner'] = 1


if __name__ == '__main__':
#     # test = [1, 2, 3, 4, [5]]
#     # print '原始数据：', test
#     # copy_t = copy(test)
#     # copy_t[0] = 5
#     # print '浅拷贝：', copy_t
#     # copy_t[-1][0] = 10
#     # print '浅拷贝：', copy_t
#     # print '原始数据：', test
#     # a = 29999
#     # print id(a)
#     # del a
#     # import time
#     # for i in range(1000):
#     #     pass
#     # b = 29999
#     # print id(b)
#     # gift = recharge_or_gift("a")
#     # print gift
#     print json.loads("\u6d3b\u52d5\u5df2\u95dc\u9589")
#     test = GameTest()
#     attr = getattr(test, "two")
#     print attr
    my_dict = {}
    my_dict['outer'] = 'auto'
    add_content(my_dict)
    print my_dict
