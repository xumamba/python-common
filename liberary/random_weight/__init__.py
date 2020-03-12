# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 下午4:51
# @Author  : serendipity-xp
# @FileName: __init__.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
"""
    带权重的随机算法：

        第一种：把所有元素key数量扩大权重倍放入数组中，普通随机该数组下标对应的元素即可；

        第二种：取出一个随机数，遍历所有元素，把各权重相加sum，当sum大于等于随机数字的时候停止，取出当前的元组；
"""