# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/19 22:28
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : list_to_queue.py
# @Software: PyCharm
"""
使用列表实现队列：
push(item) : item 入队
pop ： 出队
len： 队列长度
is_empty: 判断队列是否为空
"""
class ListQueue:

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def len(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue == []
