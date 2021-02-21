# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/20 23:57
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : Bubble_Sort.py
# @Software: PyCharm
def bubble_sort(li01):
    for i in range(len(li01) - 1):
        for x in range(i + 1, len(li01)):
            if li01[i] > li01[x]:
                li01[i], li01[x] = li01[x], li01[i]
    return li01


print(bubble_sort([2, 41, 34, 3, 2, 33, 4, 5, 8, 12]))
