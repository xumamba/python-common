#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/2 15:15

# print '({0}-{1})'.format(*[u'\u4e00', u'\u9fa5'])
print ('hello {name1}  i am {name2}'.format(name1='Kevin', name2='Tom'))

args = ['aa']
kwargs = {'name1': 'tom', 'name2': 'jerry'}
print 'hello {name1} {} i am {name2}'.format(*args, **kwargs)


def add(a, b):
    return a + b


data = [1, 2]
print add(*data)
data = {'a': 3, 'b': 4}
print add(**data)

str()