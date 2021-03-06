# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/6 23:06
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : test_x_y.py
# @Software: PyCharm
import pyautogui

currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
print(currentMouseX, currentMouseY)