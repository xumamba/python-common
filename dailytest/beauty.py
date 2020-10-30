#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xulp
# @DateTime: 2020/6/30 14:14


def beauty_data_merge(source, todo_add_intimate, addition):
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
                todo_add_intimate[s['CfgId']] = 0
                continue
            if s['IsSubdued']:
                if s['CfgId'] in todo_add_intimate.keys():
                    todo_add_intimate[s['CfgId']] += 1
                    continue
                s['AddIntimate'] += addition['AddIntimate']
                s['Intimate'] = addition['Intimate']
            else:
                s['AddFavorability'] += addition['AddFavorability']
                s['Favorability'] = addition['Favorability']
    if not same:
        source.append(addition)
    return source


def beauty_data_result(intimate_result_dict):
    for beauty_data in total_beauty_data:
        intimate_data = intimate_result_dict.get(beauty_data['CfgId'], None)
        if intimate_data:
            beauty_data['Intimate'] = intimate_data.get('Intimate', None)
            beauty_data['IntimateLv'] = intimate_data.get('IntimateLv', None)
            beauty_data['AddIntimate'] = intimate_data.get('AddIntimate', None)
            beauty_data['IsSubdued'] = intimate_data.get('IsSubdued', None)

        print '>>>beauty_data<<<:', beauty_data


def filter_event_result(event_result):
    import copy
    # 返回给客户端的数据
    result_need_award = copy.deepcopy(event_result)
    # 保存到数据库的数据
    event_data = copy.deepcopy(event_result)
    if 'event_count' in event_data:
        event_count = event_data.pop('event_count')
        result_need_award.pop('event_count')
    else:
        event_count = {}

    while True:
        # 奖励数据只下发不存入数据库
        if 'AwardList' in event_data['Extra']:
            event_data['Extra'].pop('AwardList')
        if 'event_count' in event_data:
            event_data.pop('event_count')

        # 下一个地点的事件数据
        if 'CurrentPointEventData' in event_data['Extra']:
            event_data = event_data['Extra']['CurrentPointEventData']
        else:
            break

    return result_need_award, event_data, event_count


def get_result():
    result = {
        'AddIntimate': 0,
    }
    result['AddIntimate'] += 10
    result['IntimateLv'] = 2
    result['Intimate'] = 10
    return result

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
    beauty_data_merge(total_beauty_data, add_Intimate, add_data2)
    print '2==>',  total_beauty_data, add_Intimate
    beauty_data_merge(total_beauty_data, add_Intimate, add_data3)
    print '3==>',  total_beauty_data, add_Intimate

    # event_result = {'EventId': 1, 'EventType': 8, 'event_count': {'8-1': 1}, 'EventStatus': 2,
    #                 'Extra': {'CurrentPointEventData': False, 'NextPoint': 16, 'CurrentPoint': 16}}
    # filter_event_result(event_result)

    print get_result()

    print "====>", '{host}:{port}:{user}:{pwd}:{db}:{charset}'.format(host='rm-gw8a288v8alrc745t.mysql.germany.rds.aliyuncs.com', port=3306, user='dq2readonly', pwd='dq2#local20170815', db='daqing2_character_1038_1965',
                                                                  charset='utf8')


