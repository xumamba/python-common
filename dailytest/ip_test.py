#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/6/25 14:57
import socket
import struct


def _ip_to_int(ip):
    """
    转换ip字符串为整数
    :param ip:
    :return:
    """
    return socket.ntohl(struct.unpack("I",socket.inet_aton(str(ip)))[0])


def _subnet_mask(bits):
    """
    返回首部为bits个1 的整数

    >>> _subnet_mask(8)
    >>> int("11111111 00000000 00000000 00000000")
    :param bits:
    :return:
    """
    m = 0 if bits <= 0 else 1
    zero_bits = 32 - bits
    bits -= 1
    while bits:
        m = m | (m << 1) + 1
        bits -= 1
    while zero_bits:
        m = m << 1
        zero_bits -= 1
    return m


def verify_ip_address(ip, ip_white_list):
    """
    检查某个ip是否符合指定的白名单ip列表
    :param ip: "1.234.234.111"
    :param ip_white_list: ["127.0.0.1", "192.168.0.0/16"]
    :return: bool
    """
    if not ip_white_list:
        return False

    for white_ip in ip_white_list:
        # 如果配置"0.0.0.0",则表示这个白名单配置暂时全部开放
        if '0.0.0.0' == white_ip:
            return True

        # 当白名单配置为子网时,使用子网判断,否则使用全等判断
        if '/' not in white_ip:
            if ip == white_ip:
                return True
        else:
            wip, subnet = white_ip.split('/')
            subnet = int(subnet)

            intip = _ip_to_int(ip)
            int_white_ip = _ip_to_int(wip)
            if intip & _subnet_mask(subnet) == int_white_ip & _subnet_mask(subnet):
                return True

    return False

if __name__ == '__main__':
    ip_white_list =  [
            "10.30.15.174",
            "10.19.16.91",
            "10.19.24.110",
            "10.19.26.236",
            "10.19.127.65",
            "10.60.198.230",
            "10.60.198.231",
            "10.60.198.243",
            "10.62.45.143",
            "10.61.62.190",
            "10.60.199.239",
            "10.60.0.0/15",
            "10.62.0.0/16",
            "10.52.0.0/15",
            "10.54.0.0/16",
            "10.85.8.0/21",
            "10.85.16.0/21",
            "172.29.128.0/18",
            "172.27.0.0/17"
        ]
    print verify_ip_address("10.71.153.85", ip_white_list)
