#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 AM7:27
# @Author  : L
# @Email   : L862608263@163.com
# @File    : dict.py
# @Software: PyCharm


# 字典是映射类型, 数组是序列类型
# 键: 值
dictsample = {'咸鱼': '翻身', 2: 'Two'}
# dictsample[3] = 'three'
print(dictsample['咸鱼'])
print(dictsample[2])
print(dictsample)

# 空字典
emptydict = {}

# 创建方法
dict((('f', 70), ('i', 105)))
dict(hehe='呵呵', da='哒')

# 不给值默认为None
print(emptydict.fromkeys((1, 2, 3)))
# 后面只能给一个值
print(emptydict.fromkeys((1, 2, 3), '666'))

print(dictsample.keys())
print(dictsample.values())
print(dictsample.items())

for key in dictsample.keys():
    print(key)

# 获取字典,如果不存在键会报错
# 使用get方法,有值获取值,没值就是None
dictsample.get(32)
# 也可以使用in, not in判断
print(32 in dictsample)

# 清空字典
dictsample.clear()

# ={}清空字典的方法不可靠
# a = {'1': '2'}
# b = a
#
# a = {}
#
# b还是不空

# 复制不等于浅拷贝,  copy是浅拷贝

a = {1: 'One', 2: 'Two'}
b = a.copy()
c = a

# id 打印地址

print(id(a))
print(id(b))
print(id(c))

# pop给定键,弹出对应的值
# print(dictsample.pop('咸鱼'))

# popitem随机(字典是无序的)弹一组键值

# update扔一组键值进去,替换另一个字典的对应键值
# dict.update({'key': 'value'})
