#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xumamba
# @DateTime: 2020/11/19 14:35
# @Description:

if __name__ == '__main__':
    print("=====列表局部清空=======")
    l = [1, 2, 3, 4]
    l[1:2] = (2,)
    print(l)

    print("=====字符串不可修改=======")
    strObj = "abc"
    # strObj[0] = "A"
    print(strObj)

    # s = input("please input")
    # print(s)

    print("=====& | ^=======")
    a = 37
    b = 22
    print("a=", "{:08b}".format(a))
    print("b=", "{:08b}".format(b))
    print("a&b=", "{:08b}".format(a & b))
    print("a|b=", "{:08b}".format(a | b))
    print("a^b=", "{:08b}".format(a ^ b))

    print("=====for&while的else=======")
    for i in range(5):
        print(i)
    else:
        print("for: all traversal is done")
    j = 0
    while j < 5:
        print(j)
        if j == 3:
            break
        j = j + 1
    else:
        print("while: all traversal is done")

    print("=====全局变量&局部变量=======")
    gVar = "abc"


    def alterVar():
        global gVar
        gVar = "aa"
        print(gVar)
        return


    alterVar()
    print(gVar)

    print("=====函数参数=======")


    def f(var, arr=[]):
        arr.append(var)
        return arr


    print(f(1))  # [1]
    print(f(2))  # [1, 2]

    print("=====nonlocal=======")


    def f(x):
        def inner():
            nonlocal x
            x = x + 2
            return x

        y = inner()
        return x + y


    print(f(2))  # 8

    print("=====lambda/map/filter=======")

    iterator = map(lambda x: x ** 2, [1, 2, 3, 4])
    print(iterator)  # <map object at 0x0000022D32C10EF0>
    print(list(iterator))  # [1, 4, 9, 16]

    print(tuple(map(lambda x, y: x * y, [1, 2, 3], [4, 5, 6, 7])))  # (4, 10, 18)

    print(list(filter(lambda x: x > 0, range(-5, 5))))  # [1, 2, 3, 4]

    print(dir(list))  # 显示属性
    import math

    print(help(math.fabs))  # 显示帮助文档
    # __name__ 模块名 __main__：主程序的模块名

    print("=====random=======")
    import random

    src_data = [x for x in range(1, 7)]
    random.shuffle(src_data)
    print(src_data)
    print(random.sample(src_data, 3))

    random.seed(1)
    test_seed = lambda: random.sample(range(-5, 5), 3)
    print(test_seed())  # [-3, -4, -1]
    print(test_seed())  # [-4, 2, 3]

    # 随机数发生器必须放在函数内部
    def f():
        random.seed(2)
        for i in range(5):
            print(random.random())
        for i in range(3):
            print(random.randint(-5, 5))
    f()
    f()

    def ff():
        random.seed(3)
        return random.randint(-3, 3)
    print(ff())  # -2
    print(ff())  # -2

    print("=====inner type=======")
    print((2.3-2.2) == 0.1)  # False
    print("{:04.50f}".format(2.3))  # 2.29999999999999982236431605997495353221893310546875
    print("{:04.50f}".format(2.2))  # 2.20000000000000017763568394002504646778106689453125
    print("{:04.50f}".format(0.1))  # 0.10000000000000000555111512312578270211815834045410

    import decimal
    print(decimal.Decimal(0.1))  # 0.1000000000000000055511151231257827021181583404541015625

    print("=====list=======")
    l = [1, 12, 7, 5, 9]
    for index, value in enumerate(l):
        print(index, value)
    sorted1 = sorted(l, reverse=True)  # 它不修改原来的list而是返回一个排好序的新的list
    print(sorted1)  # [12, 9, 7, 5, 1]
    print(all(l))

    import sys
    test_size = []
    print(sys.getsizeof(test_size))  # 64
    test_size = [2]
    print(sys.getsizeof(test_size))  # 72
    test_size = [2, 3.14]
    print(sys.getsizeof(test_size))  # 80
    test_size = [2, 3.14, 'hello']
    print(sys.getsizeof(test_size))  # 88
    test_size = [2, 3.14, 'hello', [5, 6.7]]
    print(sys.getsizeof(test_size))  # 96

    test_size.append('extra')
    print(sys.getsizeof(test_size))  # 128
    test_size.insert(8, 'cross border')
    print(sys.getsizeof(test_size))  # 128

    print("=====str=======")
    word = 'word '
    print(word[0])  # w

    print("=====copy=======")
    import copy
    a = ["a", 1, [2, 3]]
    b = copy.copy(a)
    c = copy.deepcopy(a)
    a.append(['str_list'])
    a[2].append(4)
    print(a)  # ['a', 1, [2, 3, 4], ['str_list']]
    print(b)  # ['a', 1, [2, 3, 4]]
    print(c)





