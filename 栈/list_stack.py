# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/19 22:15
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : list_stack.py
# @Software: PyCharm
"""
使用列表实现栈：
push(item) : item 入栈
pop()： 出栈
len()： 栈长度
is_empty(): 判断栈是否为空
"""
class ListStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def len(self):
        return len(self.stack)
