#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/5/11 14:35
import datetime
import time
from datetime import date


def strToDatetime(strTime, split='-', needMs=False):
    '''字符串转换为datetime'''
    if isinstance(strTime, datetime.datetime):
        return strTime
    if needMs:
        return datetime.datetime.strptime(strTime, "%Y" + split + "%m" + split + "%d %H:%M:%S.%f")
    return datetime.datetime.strptime(strTime, "%Y" + split + "%m" + split + "%d %H:%M:%S")


def get_one_day_start_time(date_time):
    """
    获取某天的起始时间并返回
    例如：2019-9-23 00:00:00
    :param date_time:
    :return:
    """
    date_time_str = date_time.strftime("%Y-%m-%d")
    date_time_str = date_time_str + " 00:00:00"
    one_day_start_time = strToDatetime(date_time_str)
    return one_day_start_time


def get_one_day_end_time(date_time):
    """
    获取某天的结束时间并返回
    例如：2019-9-23 23:59:59
    :param date_time:
    :return:
    """
    date_time_str = date_time.strftime("%Y-%m-%d")
    date_time_str = date_time_str + " 23:59:59"
    one_day_start_time = strToDatetime(date_time_str)
    return one_day_start_time


def checkStrIsDate(strDate):
    """检查某个字符串是否是日期"""
    if isinstance(strDate, datetime.date):
        return True

    if not isinstance(strDate, basestring):
        return False

    try:
        strDate = strDate.replace('/', '-')
        time.strptime(strDate, "%Y-%m-%d")
        return True
    except:
        return False


def strToDate(strDate, split='-'):
    """字符串转换为date"""
    if isinstance(strDate, date):
        return strDate

    d = time.strptime(strDate, "%Y" + split + "%m" + split + "%d")
    return date(d.tm_year, d.tm_mon, d.tm_mday)


if __name__ == '__main__':
    now = datetime.datetime.now()
    start_time = get_one_day_start_time(now)
    print start_time
    end_time = get_one_day_end_time(now)
    print end_time
    a = lambda x : x != ''
    print a('')
    print {} , len({'l':[]})

    data_value = '2020-05-11'
    assert checkStrIsDate(data_value)
    to_date = strToDate(data_value)
    start_time = get_one_day_start_time(to_date)
    print start_time
    end_time = get_one_day_end_time(to_date)
    print end_time

    validate = lambda x: isinstance(x, list) and len(x) != 0
    b = validate([1])
    print b
