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

    def get_linklist_head(self, head):
        # 定义两个游标
        cur = head
        pre = None
        while cur:
            # 记录下一个要操作的节点
            next_node = cur.next
            # 反转当前节点
            cur.next = pre
            # 同时移动游标
            pre = cur
            cur = next_node
        return pre


if __name__ == '__main__':
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    s = Solution()
    new_head = s.get_linklist_head(head)
    print(new_head.value)
    # 遍历反转后的链表
    while new_head:
        print(new_head.value, end="  ")
        new_head = new_head.next
    print()
