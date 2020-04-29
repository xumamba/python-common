#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/21 17:36

if __name__ == '__main__':
    next_step = [90, 365, 20]
    ladder_len = 196.06719970703
    width = next_step[0]
    distance = next_step[1]
    high_score = next_step[2]
    is_success = False
    # 判断梯子是否搭建成功
    if distance <= ladder_len <= distance + width:
        is_success = 1
        # 判断是否在高分区域
        if distance + (width - high_score) / 2 <= ladder_len <= distance + (width - high_score) / 2 + high_score:
            is_success = 2
        if width == high_score:
            is_success = 3
    print is_success