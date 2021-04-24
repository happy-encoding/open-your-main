# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/24 23:39
# @Author : GaoHan
# @Email : gaohan1130@163.com
# @File : tools.py
# @Software: PyCharm
import optparse
import os


class Tools:
    def __init__(self):
        usage = "python %prog -H <target host> -p/-P <target ports>"
        parser = optparse.OptionParser(usage)
        parser.add_option('-o', dest='old_file_path', type='string', help='old file path')
        parser.add_option('-n', '-p', dest='new_file_path', type='string', help='new file path')
        self.opts, self.args = parser.parse_args()
        self.parse_dict = {}

    def opts_obj_to_dict(self):
        try:
            print("opts object to dict")
            self.parse_dict["old_file_path"] = self.opts.old_file_path
            self.parse_dict["new_file_path"] = self.opts.new_file_path
        except Exception as e:
            print("opts object to dict Failed!!!", e)
            return 1
        print(self.parse_dict)
        return 0

    def copy_file(self):
        if self.opts_obj_to_dict() != 0:
            print("opts object to dict Failed!!!")
            return 1
        print("cp -r %s %s" % (self.parse_dict["old_file_path"], self.parse_dict["new_file_path"]))
        try:
            os.popen("cp -r %s %s" % (self.parse_dict["old_file_path"], self.parse_dict["new_file_path"]))
        except Exception as e:
            print("cp -r %s %s failed!!!,please check parse!" % (
                self.parse_dict["old_file_path"], self.parse_dict["new_file_path"]), e)
            return 1
        print("cp -r %s %s successfully!" % (self.parse_dict["old_file_path"], self.parse_dict["new_file_path"]))
        return 0

    def run(self):
        self.copy_file()


if __name__ == '__main__':
    t = Tools()
    t.run()
