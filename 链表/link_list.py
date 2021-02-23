# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/21 23:48
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : link_list.py
# @Software: PyCharm
"""
python列表实现单链表
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLink:
    """单链表类"""

    def __init__(self):
        """
        初始化一个空链表
        """
        self.head = None

    def add(self, item):
        """
        在链表头部增加节点
        :param item: 节点对象
        :return: None
        """
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """
        在链表尾部增加节点
        :param item: 需要增加的节点对象
        :return: None
        """
        node = Node(item)
        # 情况1：
        """
        if self.is_empty():
            self.add(item)
            return
        """
        if self.head == None:
            self.head = node
            return

            # 情况2：
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def remove(self, item):
        """
        移除第一个item
        :param item: 要移除的元素
        :return: None
        """
        cur = self.head
        cur2 = cur.next
        if cur.value == item:
            self.head = cur2
            return
        while cur2:
            if cur2.value == item:
                cur.next = cur2.next
                return
            cur = cur.next
            cur2 = cur.next

    def is_empty(self):
        """
        判断链表是否为空
        :return: None
        """
        # 如果头结点为空，则可以证明整个链表为空
        return self.head == None

    def len(self):
        """
        判断链表长度
        :return: 链表长度
        """
        i = 0
        cur = self.head
        while cur:
            i += 1
            cur = cur.next
        return i

    def travel(self):
        """
        遍历整个链表
        :return:
        """
        cur = self.head
        while cur:
            print(cur.value, end="  ")
            cur = cur.next
        print()

    def insert(self, index, item):
        node = Node(item)
        if self.head == None:
            self.add(node)


if __name__ == '__main__':
    s = SingleLink()
    print(s.is_empty())
    s.add(1)
    s.append(2)
    s.append(3)
    s.append(3)
    s.append(3)
    s.append(3)
    s.append(2)
    s.append(2)
    s.travel()
    print(s.is_empty())
    print(s.len())
    s.remove(2)
    s.travel()
