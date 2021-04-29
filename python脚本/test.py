# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/28 22:13
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : test.py
# @Software: PyCharm
import unittest
from unittest import mock
from python脚本.baselinebuilding import BaselineBuild


class TestBaselieBuild(unittest.TestCase):
    def test_get_build_node(self):
        # test1:
        bd = BaselineBuild("build_para.xml")
        result = bd.get_build_node()
        assert result is not None
        assert result.tag == "build"
        # test2:
        bd = BaselineBuild("")
        result = bd.get_build_node()
        assert result == 1
        # test3:
        bd = BaselineBuild("       ")
        assert result == 1

    def test_get_node(self):
        bd = BaselineBuild("build_para.xml")
        res = bd.get_child_node()


if __name__ == '__main__':
    unittest.main()
