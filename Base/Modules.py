#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 AM10:46
# @Author  : L
# @Email   : L862608263@163.com
# @File    : Modules.py
# @Software: PyCharm

# 模块(Modules)

# 直接使用random.randint  random_number = random.randint(1, 10)
# 会报错 NameError: name 'random' is not defined

# 要使用randint函数就要导入(使用import导入) random 模块

# import random
#
# random_number = random.randint(1, 10)

# 模块就是可用代码段的打包, 模块就是一个包含所有你定义的函数和变量的文件(.py)
# 模块可以被别的程序引入,以使用该模块中的函数等功能

# 下面介绍OS模块
# Operating System(操作系统)


# os模块关于文件/目录常用的函数使用方法


import os

# 函数名                         使用方法
# getcwd()                    返回当前工作目录(需要说明的是，当前目录并不是指脚本所在的目录，而是所运行脚本的目录。)
# chdir(path)                 改变工作目录
# listdir(path='.')   列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）
# mkdir(path)         创建单层目录，如该目录已存在抛出异常
# makedirs(path)      递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突
# remove(path)        删除文件
# rmdir(path)         删除单层目录，如该目录非空则抛出异常
# removedirs(path)    递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
# rename(old, new)    将文件old重命名为new
# system(command)     运行系统的shell命令
# walk(top)           遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])
#
# 以下是支持路径操作中常用到的一些定义，支持所有平台
#
# os.curdir           指代当前目录（'.'）
# os.pardir           指代上一级目录（'..'）
# os.sep              输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）
# os.linesep          当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）
# os.name             指代当前使用的操作系统（包括：'posix', & nbsp; & nbsp;'nt', 'mac', 'os2', 'ce', 'java'）

print('mulu~~~', os.getcwd())

