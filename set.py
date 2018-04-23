#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 PM5:31
# @Author  : L
# @Email   : L862608263@163.com
# @File    : set.py
# @Software: PyCharm

normalset = {1, 1, 2, 3, 4}
listset = set(list([1, 2, 3, 4]))

print(type(normalset))
print(normalset)
print(listset)

# 不可变集合
immutableset = frozenset({1, 1, 2, 3})

print(immutableset)