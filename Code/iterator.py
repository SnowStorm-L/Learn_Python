#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 PM10:22
# @Author  : L
# @Email   : L862608263@163.com
# @File    : iterator.py
# @Software: PyCharm


string = 'for语句的实现,使用了迭代器'

for idx in string:
    print(idx)

it = iter(string)

# 当next到没有元素的时候,就会抛出StopIteration的异常
# next(it)

while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)


# 迭代器里面的2个魔法方法
# def __next__(self):
# def __iter__(self):

class FibonacciSequence:
    a, b, n = 0, 1, 10

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


fi_bo = FibonacciSequence()

for each in fi_bo:
    print(each)
