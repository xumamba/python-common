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


def format_info_of_language(info):
    """根据语言类型返回相应语言信息"""
    return_info = info

    if isinstance(info, (str, unicode)):
        # 如果不全是字母,则直接使用该字符串 -- unicode的isalpha,中文会被判断为字母
        if not str(info).isalpha():
            return info
        else:
            return_info = __(info, 'zh-cn')

    elif isinstance(info, tuple):
        return_info = __(info[0], 'zn-cn')
        if not return_info:
            return_info = info[0]
        return_info = return_info % info[1:]

    return return_info


if __name__ == '__main__':
    language = format_info_of_language('defaultErrorInfo')
    print language

