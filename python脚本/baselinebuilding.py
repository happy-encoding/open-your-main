# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/28 21:06
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : baselinebuilding.py
# @Software: PyCharm

import os
from xml.etree import ElementTree


class BaselineBuild(object):
    def __init__(self, xml_file):
        self.xml_file = xml_file

    def get_build_node(self):
        """get build node object"""
        # if not self.xml_file.isfile():
        #     print("error:%s is not file" % self.xml_file)
        #     return 1
        try:
            tree = ElementTree.parse(self.xml_file)
            root = tree.getroot()
        except Exception as e:
            print("get root node failed!!!")
            return 1
        build = root.find("./build")
        return build

    def get_child_node(self, node):
        """ get node object """
        if not self.get_build_node():
            print("error: get build node failed!!!")
            return 1
        build_node = self.get_build_node()
        tool_node = build_node.find(node)
        return tool_node.text

    def generate_tool_cmd(self, node):
        filename = node.attrib["name"].strip()
        # print(filename)
        cmd = "python3 %s" % filename
        for para in node:
            if para.tag == "opt":
                cmd += " %s" % para.text.strip()
        return cmd

    def run_cmd(self, cmd):
        res = os.popen(cmd)

    def run(self):
        pass


if __name__ == '__main__':
    b = BaselineBuild("build_para.xml")
    print(b.get_child_node("./building/tool"))
