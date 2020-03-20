# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 下午4:55
# @Author  : serendipity-xp
# @FileName: wrandom.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp

import random
import json


def list_method(data):
    all_data = []
    for value, weight in data.items():
        temp = []
        for i in range(weight):
            temp.append(value)
        all_data.extend(temp)
    index = random.randint(0, len(all_data) - 1)
    return all_data[index]


def iter_method(data):
    max_weight = sum(data.values())
    rand_num = random.randint(1, max_weight)
    cur_weight = 0
    result = ""

    for key, weight in data.items():
        cur_weight += weight
        if rand_num <= cur_weight:
            result = key
            break
    return result


if __name__ == "__main__":
    test_data = {"手到擒来": 50, "轻车熟路": 25, "游刃有余": 20, "举手之劳": 5}
    iter_result = {"手到擒来": 0, "轻车熟路": 0, "游刃有余": 0, "举手之劳": 0}
    list_result = {"手到擒来": 0, "轻车熟路": 0, "游刃有余": 0, "举手之劳": 0}
    for i in range(100):
        res = iter_method(test_data)
        iter_result[res] += 1
    print json.dumps(iter_result, ensure_ascii=False, encoding='UTF-8')
    print '-' * 56
    for i in range(100):
        res = list_method(test_data)
        list_result[res] += 1
    print json.dumps(list_result, ensure_ascii=False, encoding='UTF-8')
    for i in range(10):
        print random.choice([True, False])
