#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/26 16:34
import random


def get_red_bag(golds, person):
    """
    非递归算法：
    红包算法3.0
    :param golds: 剩余的元宝数目
    :param person: 还可以领取红包的人数
    :return:
    """
    red_list = list()
    red_expect = int(golds / person)

    if golds < 1 or golds < person:
        return False

    # 只有一个红包的情况
    if person == 1:
        red_list.append(golds)
    count = 0
    for i in xrange(person / 2):
        # 第一个红包的领取情况
        red = random.randint(1, red_expect * 2 - 1)
        red_list.append(red)

        # 第 i + person / 2 个红包（红包两两配对）
        red_list.append(red_expect * 2 - red)

        # 统计一共被领取多少元宝
        count += red + (red_expect * 2 - red)
    # 是否还有剩余的元宝没有被领取，有的话随机给一个补上剩余的元宝
    count_left = golds - count
    if count_left >= 0:
        red_list[0] += count_left
    # 打乱红包列表
    random.shuffle(red_list)
    return red_list


if __name__ == '__main__':
    result = get_red_bag(80, 10)
    print result
