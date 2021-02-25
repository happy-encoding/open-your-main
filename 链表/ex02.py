# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/24 22:56
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : ex02.py
# @Software: PyCharm
"""
输入一个链表，反转链表后，输出新链表的表头
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_linklist_head(self,head):
        cur = head
        pre = None
        while True:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


