# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/3 23:00
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : demo02.py
# @Software: PyCharm
import sys

# 获取参数  （列表）
print(sys.argv)
# 返回模块可以搜索到的环境变量
print(sys.path)
# 添加环境变量
# sys.path.append("BASH_DIR")
print(sys.path)
# 获取当前平台（win，linux，unix）
print(sys.platform)

# sys.exit() 异常退出
# for i in range(5):
#     if i ==3:
#         sys.exit(3)
#     print(i)
# 获取python解释器版本
print(sys.version)