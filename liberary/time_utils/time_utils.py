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


def str_to_timestamp(datatime_str):
    """
    时间转换为时间戳
    :param datatime_str:
    :return:
    """
    return time.mktime(time.strptime(datatime_str, '%Y-%m-%d %H:%M:%S'))


def timestamp_to_str(dt):
    """
    转换str时间为时间戳
    :param dt: str
    """
    time_struct = time.localtime(dt)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)


def datetime_to_timestamp(dt):
    """
    日期时间转时间戳
    :param dt: 日期时间
    :return: 时间戳
    """
    if not isinstance(dt, basestring):
        dt = '{dt_str}'.format(dt_str=dt)
    return int(time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S')))


if __name__ == '__main__':
    # now = datetime.datetime.now()
    # start_time = get_one_day_start_time(now)
    # print start_time
    # end_time = get_one_day_end_time(now)
    # print end_time
    # a = lambda x : x != ''
    # print a('')
    # print {} , len({'l':[]})
    #
    # data_value = '2020-05-11'
    # assert checkStrIsDate(data_value)
    # to_date = strToDate(data_value)
    # start_time = get_one_day_start_time(to_date)
    # print start_time
    # end_time = get_one_day_end_time(to_date)
    # print end_time
    #
    # validate = lambda x: isinstance(x, list) and len(x) != 0
    # b = validate([1])
    # print b
    timestamp = str_to_timestamp("2020-06-17 23:59:59")
    print timestamp
    print timestamp_to_str(timestamp)
    to_timestamp = datetime_to_timestamp("2020-06-17 23:59:59")
    print to_timestamp
    dt = datetime.datetime(2020,06,17,23,59,59)
    print 'dt:', dt, type(dt)
    print '{dt}'.format(dt=dt)
    print datetime_to_timestamp('{dt}'.format(dt=dt))
    print '================================='
    print datetime_to_timestamp(datetime.datetime(2020, 06, 17, 23, 59, 59))
