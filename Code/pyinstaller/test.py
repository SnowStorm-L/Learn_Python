#!/usr/local/bin/python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 PM9:59
# @Author  : L
# @Email   : L862608263@163.com
# @File    : test.py
# @Software: PyCharm

import os

os.system("which python")

# 该工具的官网文档
# https://pyinstaller.readthedocs.io/en/v3.3.1/usage.html

# 以这个文件作为演示

# pyinstaller命令的语法为:
# pyinstaller [options] script [script …] | specfile

# 最简单的演示, cd到pyinstaller目录下, 然后执行:
# pyinstaller test.py

# PyInstaller会分析test.py文件, 然后做以下几件事情
# 1, 将test.spec写入与test.py相同的文件夹中。
# 2, 在test.py相同的文件夹中创建build文件夹, 如果build文件夹不存在的话.
# 3, 在build文件夹中写入一些日志文件和工作文件。
# 4, 在test.py相同的文件夹中创建dist文件夹, 如果dist文件夹不存在的话.
# 5, 将test.py可执行文件夹写入dist文件夹中。

# 在dist文件夹中，您可以找到分发给用户的打包好的应用程序。

# 打包的exe 并不是跨平台使用, 就是你在mac打包的exe还是只能在mac运行, 不能直接放到win上运行
# 只能把代码放到win上打包
