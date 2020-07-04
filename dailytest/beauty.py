#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xulp
# @DateTime: 2020/6/30 14:14


def beauty_data_merge(source,todo_add_Intimate, addition):
    """
    美人数据合并
    """
    same = False
    for s in source:
        if s['CfgId'] == addition['CfgId']:
            same = True
            if s['IsSubdued'] != addition['IsSubdued']:
                # 中途获得妃子，从此加亲密度
                s['IsSubdued'] = addition['IsSubdued']
                todo_add_Intimate[s['CfgId']] = 0
                continue
            if s['IsSubdued']:
                todo_add_Intimate[s['CfgId']] += 1
                # s['Intimate'] = addition['Intimate']
            else:
                s['AddFavorability'] += addition['AddFavorability']
                s['Favorability'] = addition['Favorability']
    if not same:
        source.append(addition)
    return source


if __name__ == '__main__':
    total_beauty_data = []
    add_Intimate = {}  # key:待添加亲密度的妃子，value:待添加亲密度的次数
    add_data1 = {'AddFavorability': 1,
                'Favorability': 10,
                'FavorabilityMax': 10,
                'IsSubdued': False,
                'CfgId': 1}
    add_data2 = {'AddFavorability': 1,
                'Favorability': 10,
                'FavorabilityMax': 10,
                'IsSubdued': True,
                'CfgId': 1}
    add_data3 = {'AddFavorability': 1,
                'Favorability': 10,
                'FavorabilityMax': 10,
                'IsSubdued': True,
                'CfgId': 1}
    beauty_data_merge(total_beauty_data, add_Intimate, add_data1)
    print '1==>', total_beauty_data, add_Intimate
    for key, value in add_Intimate.iteritems():
        print key
        print value
    beauty_data_merge(total_beauty_data, add_Intimate, add_data2)
    print '2==>',  total_beauty_data, add_Intimate
    beauty_data_merge(total_beauty_data, add_Intimate, add_data3)
    print '3==>',  total_beauty_data, add_Intimate
    for key, value in add_Intimate.iteritems():
        print key
        print value


