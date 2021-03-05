# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 23:26
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : attack_guazicar.py
# @Software: PyCharm
import requests
url = "https://www.guazi.com/wh/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
resp= requests.get(url=url,headers=headers)
html = resp.content
print(html)