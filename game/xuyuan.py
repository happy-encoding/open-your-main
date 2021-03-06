# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/6 21:54
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : xuyuan.py
# @Software: PyCharm
import pyautogui, time

currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
print(currentMouseX, currentMouseY)
# pyautogui.moveTo(1581, 1067)
print("打开游戏")
pyautogui.click(x=1581, y=1067, duration=2)  # 先移动到(100, 200)再单击
# 962 757
while True:
    print("点击许愿池")
    pyautogui.click(x=962, y=757, duration=0.5)
    print("点击我愿意")
    pyautogui.click(x=960, y=659,duration=0.2)
    print("等待35s广告。。。")
    time.sleep(35)
    print("关闭广告")
    pyautogui.click(x=1145, y=189, duration=0.2)
    print("等待35s，进入下次许愿。。。")
    time.sleep(35)
