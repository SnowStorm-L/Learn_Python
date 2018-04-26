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

# 函数名                                                   使用方法
# getcwd()                                        返回表示当前工作目录的字符串。
# chdir(path)                                     将当前工作目录更改为path.
# listdir(path='.')                               列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）
# mkdir(path, mode=0o777)                         创建单层目录,如该目录已存在抛出异常mode文件权限可以查看http://www.111cn.net/sys/linux/59979.htm
#
# makedirs(name, mode=0o777, exist_ok=False)      递归创建多层目录,如该目录已存在抛出异常exist_ok该参数为True时执行mkdir -p，但如果给出了mode参数，
#                                                 目标目录已经存在并且与即将创建的目录权限不一致时，会抛出OSError异常
#
# remove(path)                                              删除文件
# rmdir(path)                                               删除单层目录，如该目录非空则抛出异常
# removedirs(path)                                          递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
# rename(old, new)                                          将文件old重命名为new
# system(command)                                           运行系统的shell命令 e.g (os.system('open -a Terminal.app'))
# walk(top, topdown=True, onerror=None, followlinks=False)) 遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])
#
# 以下是支持路径操作中常用到的一些定义，支持所有平台
#
# os.curdir           指代当前目录（'.'）
# os.pardir           指代上一级目录（'..'）
# os.sep              输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）
# os.linesep          当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）
# os.name             指代当前使用的操作系统（包括：'posix', 'nt', 'mac', 'os2', 'ce', 'java'）

path = '/Users/l/Desktop/LearnPython'

print(os.linesep)
print(os.name)

print(list(os.walk(path)))

# os.path模块中关于路径常用的函数使用方法

# 函数名                                                 使用方法
# basename(path)                  去掉目录路径，单独返回文件名
# dirname(path)                   去掉文件名，单独返回目录路径
# join(path1[, path2[, ...]])     将path1, path2各部分组合成一个路径名
# split(path)                     分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在
# splitext(path)                  分离文件名与扩展名，返回(f_name, f_extension)元组
# getsize(file)                   返回指定文件的尺寸，单位是字节
# getatime(file)                  返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
# getctime(file)                  返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
# getmtime(file)                  返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
#
# 以下为函数返回True或False
#
# exists(path)            判断指定路径（目录或文件）是否存在
# isabs(path)             判断指定路径是否为绝对路径
# isdir(path)             判断指定路径是否存在且是一个目录
# isfile(path)            判断指定路径是否存在且是一个文件
# islink(path)            判断指定路径是否存在且是一个符号链接
# ismount(path)           判断指定路径是否存在且是一个挂载点
# samefile(path1, paht2)  判断path1和path2两个路径是否指向同一个文件
