# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 23:26
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : attack_guazicar.py
# @Software: PyCharm
import requests
url = "https://www.guazi.com/wh/"
resp= requests.get(url=url)
html = resp.content
print(html)