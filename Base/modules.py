#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 AM10:46
# @Author  : L
# @Email   : L862608263@163.com
# @File    : modules.py
# @Software: PyCharm

# 模块(Modules)

# 直接使用random.randint  random_number = random.randint(1, 10)
# 会报错 NameError: name 'random' is not defined

# 要使用randint函数就要导入(使用import导入) random 模块

# 导入方法1

# import 模块名

# 如果使用上面这种形式导入的话,那么使用模块的函数的时候,必须在函数的前面加上前缀模块名
# 例如 模块名.方法()

# 导入方法2

# from 模块名 import (* 或 f1, f2 具体方法名)

# 这使得我们更容易调用模块的函数,但是有其它问题,例如你导入的库的函数名与你本类的方法名重复了,会覆盖掉

# 导入方法3

# import 模块名 as 自定义模块别名

# 这种方法比较推荐,既能保持模块的命名空间,又能减少前缀的代码数


# import random
#
# random_number = random.randint(1, 10)

# 模块就是可用代码段的打包, 模块就是一个包含所有你定义的函数和变量的文件(.py)
# 模块可以被别的程序引入,以使用该模块中的函数等功能


# 模块单独功能测试
# 如果想函数在本模块运行, 而不在被导入的模块运行(测试本模块的代码可用性)
# 可以使用 if __name__ == '__main__' 做判断

# 在自己模块中打印

# print(__name__)  # __main__

# 在导入的模块中打印

# print(模块实例对象.__name__)  # modules


# 搜索路径
# 模块的导入会进行一个搜索路径的过程
# 例如你导入一个hello模块, py会在预定好的模块搜索路径找这个模块, 找到了就导入, 找不到就导入失败

import sys

# py的模块搜索路径
# 这里是个列表,可以append自己的模块路径
print(sys.path)

# 模块的推荐存放路径site-packages
# /Users/l/Desktop/LearnPython/venv/lib/python3.6/site-packages


# 包(package)
# 1, 创建一个文件夹, 用于存放相关的模块, 文件夹的名字即包的名字
# 2, 在文件夹中创建一个__init__.py的模块文件, 内容可以为空
# 3, 将相关的模块,放入文件夹中


# 导入
# 包名(文件夹名).模块名


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
# walk(top, topdown=True, onerror=None, followlinks=False))
# 遍历top路径以下所有的子**目录(只是目录)，top返回一个三元组：(路径, [包含目录], [包含文件])
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
# islink(path)            判断指定路径是否存在且是一个符号链接(windows上就是快捷方式)
# ismount(path)           判断指定路径是否存在且是一个挂载点(例如C盘,D盘这些就是挂载点)
# samefile(path1, paht2)  判断path1和path2两个路径是否指向同一个文件
