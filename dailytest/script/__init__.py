#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/23 17:40

import requests
import json


def req(action_id,
        data,
        rid=None,
        server_id=None,
        app_id=None,
        url='http://127.0.0.1:30003/frontend_stateless'):

    data['Rid'] = rid or "708e1dcf74c611eaabbe40b076def685"
    data['ActionId'] = action_id
    data['ServerId'] = server_id or 24
    data['AppId'] = app_id or 1010
    data['Ver'] = '2.5'
    print 'Request:', data

    res = requests.post(url, json=data)
    if res.status_code != 200:
        print 'Error:', res
        return

    data_res = json.loads(res.content)
    print 'Response:', json.dumps(data_res, indent=4, ensure_ascii=False)

    return data_res


if __name__ == '__main__':
    while True:
        req(11008,
            {"HotVer": "", "MinisterId": 15, "FruitType": 2, "ActionId": 11008, "UseNum": 10, "Ver": "2.9",
             "ServerId": 23, "actionid": 11008, "Rid": "708e1dcf74c611eaabbe40b076def685", "GoodThings": 2093422502,
             "Lang": "zh-cn", "AppId": 1111}
            )

