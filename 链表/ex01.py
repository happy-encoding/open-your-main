# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/24 22:29
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : ex01.py
# @Software: PyCharm
"""
输入一个链表，从尾到头返回一个ArrayList
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_array_list(self, head):
        array_list = []
        cur = head
        while cur:
            array_list.append(cur.value)
            cur = cur.next
        array_list.reverse()
        # array_list=array_list[::-1]
        return array_list


if __name__ == '__main__':
    # 创建链表
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    s = Solution()
    print(s.get_array_list(head))
