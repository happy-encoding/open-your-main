# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/23 23:34
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : demo01.py
# @Software: PyCharm
import os, sys

# cmd 执行命令
#  1.有返回值
# msg = os.popen("date")
# #  2.无返回值
# os.system("date")

# 检测访问权限  参数1： 路径
# 参数二： os.F_OK:路径是否存在；
#          os.R_OK:是是否有可读权限；
#           os.W_OK:是是否有可写权限；
#           os.X_OK:是是否有可执行权限；
# msg = os.access("D:", os.X_OK)
# print(msg)

# 查看当前工作目录
# msg = os.getcwd()
# msg = os.path.dirname(__file__)
# print(msg)
# os.chdir("D:")
print(os.getcwd())

