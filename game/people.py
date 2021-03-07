# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/7 16:49
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : people.py
# @Software: PyCharm
import pyautogui, time

# print(time.time())
print("打开游戏")
pyautogui.click(x=1581, y=1067, duration=2)
i = 0
while i < 50:
    i += 1
    begin_time = time.time()
    while True:
        end_time = time.time()
        if end_time-begin_time>60:
            break
        pyautogui.click(x=1130, y=878)
    time.sleep(20)
