#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 AM10:22
# @Author  : L
# @Email   : L862608263@163.com
# @File    : generator.py
# @Software: PyCharm

# 生成器的发明使python模仿协同程序的方法得以实现
# 所谓的协同程序就是可以运行独立函数调用,函数可以暂时或者挂起,并在需要的时候从程序离开的地方继续或者重新开始


def my_generator():
    print('生成器被执行 !')
    yield 1
    yield 2


demo = my_generator()
print(next(demo))
print(next(demo))


# next(demo) StopIteration


def test():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


for each in test():
    if each > 100:
        break
    print(each, end=" ")
