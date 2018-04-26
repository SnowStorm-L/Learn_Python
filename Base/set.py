#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 PM5:31
# @Author  : L
# @Email   : L862608263@163.com
# @File    : set.py
# @Software: PyCharm


# 集合是无序,唯一的
# {}之内没有固定的对应关系,就会被认为是集合(set)

normalset = {1, 1, 2, 3, 4}
listset = set(list([1, 2, 3, 4]))

print(type(normalset))
print(normalset)
print(listset)

# for in 把集合元素读取出来

for each_value in normalset:
    print(each_value)

# in, not in 判断元素是否在集合内

print(5 in normalset)
print(5 not in normalset)

# add, remove  添加/移除 集合中的元素
normalset.add(5)
normalset.remove(1)

print(normalset)

# 不可变集合
immutableset = frozenset([1, 1, 2, 3])

print(immutableset)
