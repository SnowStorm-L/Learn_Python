#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 5:39 PM
# @Author  : L
# @Email   : L862608263@163.com
# @File    : tkinter_learn.py
# @Software: PyCharm

# NOTE tkinter -- Tcl/Tk的Python接口

# Tk和tkinter都可以在大多数Unix平台以及Windows系统上使用。
# Tk本身不是Python的一部分; 它保存在ActiveState中。

# 在命令行中运行 python -m tkinter，应该会弹出一个Tk界面的窗口，
# 表明 tkinter 包已经正确安装，而且告诉你 Tcl/Tk 的版本号，通过这个版本号，你就可以参考对应的 Tcl/Tk 文档了。

# NOTE Tkinter 模块

# 在大多数时候你只需要 tkinter 就足够了，但也有一些额外的模块可供使用。
# Tk 接口位于一个名字为_tkinter 的二进制模块当中。
# 此模块包含了低层级的 Tk 接口，它不应该被应用程序员所直接使用。
# 它通常是一个共享库（或DLL），但在某些情况下也可能被静态链接到 Python 解释器。

# 除了Tk接口， tkinter 也包含了若干 Python 模块，tkinter.constants 是其中最重要的。
# 导入 tkinter 会自动导入 tkinter.constants ，所以，要使用 Tkinter 通常你只需要一条简单的 import 语句:

import tkinter

# 或者更常用的:

from tkinter import *

# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

