#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xulp
# @DateTime: 2020/4/23 17:40


if __name__ == '__main__':
    i = 0
    while True:
        di = dict()
        di["test"] = 'a' or 'b'
        assert di['test'] == 'a'

        di["test1"] = None or 'b'
        assert di['test1'] == 'b'

        i += 1
        print i