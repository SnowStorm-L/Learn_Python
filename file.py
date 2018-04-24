#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 AM10:54
# @Author  : L
# @Email   : L862608263@163.com
# @File    : file.py
# @Software: PyCharm

# file文件操作

# 打开文件
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 除了第一个要,其它都有默认参数
# file是文件路径
# mode是设置文件打开的模式

# TODO 这里几种模式可以组合使用, 具体迟点再研究, 这个文件模式是 Python 从C 的fopen()调用中复制模式

# model有以下几个选择(可多选)
# 'r'以只读方式打开文件（默认）
# 'w'以写入的方式打开文件，会覆盖已存在的文件
# 'x'创建一个新文件并打开它进行写入
# 'a'开放写入，如果存在则附加到文件末尾
# 'b'二进制模式
# 't'文本模式（默认）
# '+'打开磁盘文件进行更新（读取和写入）
# 'U'通用换行符模式（已弃用）

# 文件对象方法

# 文件对象方法                            执行操作
# f.close()                                                 关闭文件
# f.read(self, n: int = -1))            从文件读取n个字符，当未给定n或给定负值的时候，读取剩余的所有字符，然后作为字符串返回
# f.readline(self, limit: int = -1)     从文件中读取并返回一行（包括行结束符），如果有limit有定义则返回limit个字符
# f.write(str)                          将字符串str写入文件
# f.writelines(lines: List[AnyStr]))    向文件写入字符串序列list，list应该是一个返回字符串的可迭代对象
# f.seek(offset: int, whence: int = 0)  在文件中移动文件指针，从whence（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节
# f.tell()                              返回当前在文件中的位置
# f.truncate(size: int = None))         截取文件到size个字节，默认是截取到文件指针当前位置

file = open('/Users/l/Desktop/pyTest.txt', 'r+')

print('文件对象--', file)

# 第一次读的话,会默认全部读取
# 如果再调用一次读的方法的话,会没有任何输出
# 因为第一次读完的时候,文件指针已经在末尾
# print('文件内容--', file.read())

print('读当前指针位置的后5个--', file.read(5))

print('当前指针位置--', file.tell())

print('修改指针位置', file.seek(5, 0))

print('读取指针位置当前行--', file.readline())

print('list将文件对象转换为列表--', list(file))

file.seek(0, 0)
for each_line in file:
    print(each_line)

file.write('jjyy')

# 打开对应关闭, 打开和关闭之间是操作
# 关闭文件
file.close()
