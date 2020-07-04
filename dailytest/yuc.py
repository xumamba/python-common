# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 下午8:35
# @Author  : serendipity-xp
# @FileName: yuc.py
# @Software: PyCharm
# @GitHub  ：https://github.com/serendipity-xp
import unittest


class TestDaemon(unittest.TestCase):
    def test_list(self):
        list1 = [123, 456, 789, 123, 456]
        self.assertTrue(123 in list1)
        self.assertEqual(5, len(list1))
        self.assertEqual(2, list1.index(789))
        self.assertEqual(3, list1.index(123, 2, 4))

        list1.reverse()
        print(list1)
        list1.sort()
        print(list1)
        list1.sort(reverse=True)
        print(list1)

    def test_tuple(self):
        t = (1, 2, 3, 4, 5)  # 1，
        print(t)
        self.assertTrue(isinstance(t, tuple))
        t2 = 8 * (2,)
        print(t2)
        t2 = t2[:2] + (1,) + t2[2:]
        print(t2)

    def test_str(self):
        str1 = 'I love golang'
        print(str1[7])

    def test_dict(self):
        print '\ntest_dict'
        test_dict = dict()
        test_dict['one'] = 1
        test_dict['two'] = {"two1": 2}
        print test_dict

    def test_coding(self):
        u_str = u'["2"]'

    def test_pop(self):
        pass