# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 23:44
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : headers_test.py
# @Software: PyCharm
"""
向测试网站发请求，确认请求头中User-Agent？
"""
import requests

url = "http://httpbin.org/get"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
html = requests.get(url=url, headers=headers).text
print(html)
