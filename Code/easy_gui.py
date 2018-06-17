#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 PM3:46
# @Author  : L
# @Email   : L862608263@163.com
# @File    : easy_gui.py
# @Software: PyCharm

# python 做UI的 有以下几个库
# easyGUI < Tkinter(自带的) < PyQT5

# 安装easyGUI

# command + , 进入 preference
# 输入interpreter
# 输入库名 install package

# 导入方法1

# import easygui

# 如果使用上面这种形式导入的话,那么使用EasyGui的函数的时候,必须在函数的前面加上前缀easygui
# 例如 easygui.msgbox()

# 导入方法2

# from easygui import *

# 这使得我们更容易调用EasyGui的函数,但是有其它问题,例如你导入的库的函数名msgbox与你本类的方法名重复了,会覆盖掉
# 例如 msgbox()

# 导入方法3
# 这种方法比较推荐,既能保持easygui的命名空间,又能减少前缀的代码数

import os
import easygui as g
import random


class GuessNumber:

    # noinspection PyMethodMayBeStatic
    def start(self):
        g.msgbox('嗨,欢迎进入第一个界面小游戏')
        secret = random.randint(1, 10)
        msg = '猜一个数字'
        title = "数字小游戏"

        guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)

        while True:
            if guess == secret:
                g.msgbox('猜对了')
                break
            else:
                if guess > secret:
                    g.msgbox('大了')
                else:
                    g.msgbox('小了')

                guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
        g.msgbox('游戏结束')


class UserInfo:

    # noinspection PyMethodMayBeStatic
    def start(self):
        msg = "请填写以下联系方式"
        title = "账号中心"
        field_names = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', 'E-mail']
        field_values = g.multenterbox(msg, title, field_names)

        while 1:
            if field_values is None:
                break
            err_msg = ""
            for i in range(len(field_names)):
                option = field_names[i].strip()
                if field_values[i].strip() == "" and option[0] == "*":
                    err_msg += ("[%s]为必填项. \n\n" % field_names[i])
            if err_msg == "":
                break
            field_values = g.multenterbox(err_msg, title, field_names)

        print('用户资料如下: %s' % (str(field_values)))


class CodeStatistics:
    source_list = {}
    file_list = {}
    target = ['.js', '.html', '.css', '.m', '.swift', '.py']

    def start(self):
        g.msgbox("打开存放代码的文件...", "统计代码量")
        code_path = g.diropenbox("选择代码库:")
        self.search_file(code_path)
        self.show_result()

    def show_result(self):
        total = 0
        text = ''
        for i in self.source_list:
            lines = self.source_list[i]
            total += lines
            text += '[%s] 源文件 %d 个, 源代码 %d 行\n' % (i, self.file_list[i], lines)
        title = '统计结果'
        msg = '目前累积编写了 %d 行代码' % total
        g.textbox(msg, title, text)

    # noinspection PyMethodMayBeStatic
    def calc_code(self, file_name):
        lines = 0
        with open(file_name) as f:
            print('正在分析文件: %s ...' % file_name)
            try:
                for _ in f:
                    lines += 1
            except UnicodeDecodeError:
                pass  # 文件格式不兼容, 忽略掉
        return lines

    def search_file(self, in_path):

        file_list = os.listdir(in_path)

        for filename in file_list:

            file_path = os.path.join(in_path, filename)

            if os.path.isdir(file_path):
                self.search_file(file_path)
            else:
                file, ext = os.path.splitext(file_path)
                if ext is None:
                    continue
                if ext in self.target:
                    lines = self.calc_code("{0}{1}".format(file, ext))  # 统计行数
                    # 如果字典中不存,抛出KeyError,则添加字典键
                    # 统计文件数
                    try:
                        self.file_list[ext] += 1
                    except KeyError:
                        self.file_list[ext] = 1

                    # 统计源代码行数
                    try:
                        self.source_list[ext] += lines
                    except KeyError:
                        self.source_list[ext] = lines


# GuessNumber().start()
# UserInfo().start()
# CodeStatistics().start()

# 用pipenv导入不识别头文件, 可以在Project Interpreter用pip3导入


# import sys
#
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
#
# app = QApplication(sys.argv)
