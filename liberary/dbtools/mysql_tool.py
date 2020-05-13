#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/5/7 17:01
import pymysql
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB

PoolDict = {}


def get_pool(host, port, user, pwd, db, charset):
    return PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=0,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=1,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。
    # 如：0 = None = never,
    # 1 = default = whenever it is requested,
    # 2 = when a cursor is created,
    # 4 = when a query is executed,
    # 7 = always
    host=host,
    port=port,
    user=user,
    password=pwd,
    database=db,
    charset=charset
    )


def get_conn(host, port, user, passwd, db, charset='utf8', use_dict_cursor=True):
    pool = PoolDict[host+port]
    if not pool:
        pool = get_pool(host, port, user, passwd, db, charset)
        PoolDict[host + port] = pool
    conn = pool.connection()
    if use_dict_cursor:
        cursor = conn.cursor(DictCursor)
    else:
        cursor = conn.cursor()
    return conn, cursor
