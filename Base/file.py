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

file.write('test_str')

# 打开对应关闭, 打开和关闭之间是操作
# 关闭文件
file.close()

# *********************************************#
#        异常处理配合with语句                   #
#            可以避免已打开文件没关闭的情况       #
# *********************************************#
try:
    with open('data.txt', 'w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦：' + str(reason))


# 小练习

# 在桌面创建一个名为record.txt的文件 把以下内容去掉注释, 复制进record.txt

# 小客服：小甲鱼，今天有客服问你有没有女朋友？
# 小甲鱼：咦？
# 小客服：我跟她说你有女朋友了！
# 小甲鱼：。。。。。。。
# 小客服：她让你分手后考虑下她！然后我说：“您要买个优盘，我就帮您留意下~”
# 小甲鱼：然后呢？
# 小客服：她买了两个，说发一个货就好~
# 小甲鱼：呃。。。。。。你真牛！
# 小客服：谁让我是鱼C最可爱的小客服嘛~
# 小甲鱼：下次有人想调戏你我不阻止~
# 小客服：滚！！！
# ======================================================================================
# 小客服：小甲鱼，有个好评很好笑哈。
# 小甲鱼：哦？
# 小客服：“有了小甲鱼，以后妈妈再也不用担心我的学习了~”
# 小甲鱼：哈哈哈，我看到丫，我还发微博了呢~
# 小客服：嗯嗯，我看了你的微博丫~
# 小甲鱼：哟西~
# 小客服：那个有条回复“左手拿着小甲鱼，右手拿着打火机，哪里不会点哪里，so easy ^_^”
# 小甲鱼：T_T
# =======================================================================================
# 小客服：小甲鱼，今天一个会员想找你
# 小甲鱼：哦？什么事？
# 小客服：他说你的一个学生月薪已经超过12K了！！
# 小甲鱼：哪里的？
# 小客服：上海的
# 小甲鱼：那正常，哪家公司？
# 小客服：他没说呀。
# 小甲鱼：哦
# 小客服：老大，为什么我工资那么低啊？？是时候涨工资了！！
# 小甲鱼：啊，你说什么？我在外边呢，这里好吵吖。。。。。
# 小客服：滚！！

# 练习要求
# 任务：将文件（record.txt）中的数据进行分割并按照以下规律保存起来：
# -小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼：”）
# -小客服的对话单独保存为girl_*.txt的文件（去掉“小客服：”）
# -文件中总共有三段对话，分别保存为boy_1.txt，girl_1.txt，boy_2.txt，
# girl_2.txt，boy_3.txt，girl_3.txt共6个文件（提示：文件中的不同对话见已经使用“=========”分割）

# 以下属性命名可能和上面的重复, 注释一下就好

# def create_file(filename, write_content):
#
#     file = open('/Users/l/Desktop/{0}.txt'.format(filename), mode='x')
#
#     file.writelines(write_content)
#
#     file.close()
#
#
# def split_file():
#
#     origin_file = open('/Users/l/Desktop/record.txt')
#
#     file_content_dict = {}
#
#     index = 0
#
#     for each_line in origin_file:
#
#         if '===' in each_line:
#
#             index += 1
#
#             continue
#
#         else:
#
#             (people, content) = each_line.split('：', 1)
#
#             file_content_dict[people] = '{0}{1}'.format(file_content_dict.get(people), content)
#
#             sub_filename = '{0}_{1}'.format('boy' if people == '小甲鱼' else 'girl', index)
#
#             file_content_dict[sub_filename] = '{0}{1}'.format(file_content_dict.get(sub_filename), content)
#
#     origin_file.close()
#
#     return file_content_dict
#
#
# for key in split_file().keys():
#
#     create_file(key, list(split_file().get(key)))

# 编写一个程序,接受用户输入并保持为新的文件

# def file_write(file_name):
#     try:
#         with open('/Users/l/Desktop/{0}.txt'.format(file_name), 'w') as input_file:
#             print("请输入内容[单独输入':w'保存退出]:")
#             while True:
#                 input_content = input()
#                 if input_content == ":w":
#                     break
#                 input_file.write('%s\n' % input_content)
#
#     except OSError as reason:
#         print('出错啦：' + str(reason))
#
#
# input_file_name = input('请输入文件名:')
# file_write(input_file_name)
