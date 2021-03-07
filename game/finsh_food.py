# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/6 23:27
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : finsh_food.py
# @Software: PyCharm
import pyautogui, time

currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
print(currentMouseX, currentMouseY)
# pyautogui.moveTo(1581, 1067)
print("打开游戏")
pyautogui.click(x=1581, y=1067, duration=2)  # 先移动到(100, 200)再单击
# 962 757
print("点击渔夫")
pyautogui.click(x=845, y=503, duration=1)
print("增加饲料")
pyautogui.click(x=968, y=245, duration=1)
i = 1
while i < 15:
    try:
        i += 1
        print(i)
        print("点击观看广告获取饲料")
        pyautogui.click(x=1033, y=547, duration=1)
        print("等待35s广告。。。")
        time.sleep(35)
        print("关闭广告")
        pyautogui.click(x=1137, y=184, duration=1)
    except Exception as e:
        print(e)
# 点击空白 358 616
pyautogui.click(x=828, y=839, duration=1)
# 点击x号 778  902
pyautogui.click(x=776, y=895, duration=1)
# 点击向右 1163  549
pyautogui.click(x=1159, y=547, duration=1)
while i < 80:
    try:
        print(i)
        print("点击许愿池")
        pyautogui.click(x=962, y=757, duration=1)
        print("点击我愿意")
        pyautogui.click(x=960, y=659, duration=1)
        print("等待35s广告。。。")
        time.sleep(35)
        print("关闭广告")
        pyautogui.click(x=1145, y=189, duration=1)
        print("等待35s，进入下次许愿。。。")
        time.sleep(35)
    except Exception as e:
        print(e)
