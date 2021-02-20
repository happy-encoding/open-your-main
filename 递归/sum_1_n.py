# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/20 23:38
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : sum_1_n.py
# @Software: PyCharm
"""
利用递归算法求n-m之间所有整数和
"""


def sum(n, m):
    if n == m:
        return n
    elif n > m:
        return n + sum(n - 1, m)
    elif n < m:
        return n + sum(n + 1, m)



