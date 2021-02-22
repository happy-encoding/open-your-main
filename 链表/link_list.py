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
        pass

    def append(self, item):
        """
        在链表尾部增加节点
        :param item: 需要增加的节点对象
        :return: None
        """
        pass

    def remove(self):
        pass

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
        pass

    def travel(self):
        pass
