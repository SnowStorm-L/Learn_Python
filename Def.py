#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 PM4:37
# @Author  : L
# @Email   : L862608263@163.com
# @File    : Def.py
# @Software: PyCharm

import logging

# 定义
# def 定义函数的关键字

# 默认参数 num2


def add(num1, num2=5):
    """函数说明"""
    return num1 + num2


# 调用
print(add(5, 6))
# 函数说明
print(add.__doc__)

# print(help(add))


# 关键字参数

print(add(num1=1))

# 收集参数(可变参数) ***再加其它参数的话,要加默认参数,或者调用的时候用关键字参数


def test(*parameter, exp):
    """用元组打包起来, 命名为parameter的元组"""
    print('参数的长度是', len(parameter))
    print('第一个参数是', parameter[0])
    print(exp)


test(1, 2, 3, '4', exp='8')


def hello():
    print("666")


temp = hello()

# None
print(temp)
# <class 'NoneType'>
print(type(temp))

# 调用函数,没返回值就返回None


# 返回多个值, 元组或者序列

def back():
    return [1, "2"]


# 嵌套函数

def checkparams(fn):
    def wrapper(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return fn(a, b)
        logging.warning("variable 'a' and 'b' can't not be add")
        return
    return wrapper


add = checkparams(add)
add(3, 'test')

@checkparams
def add(a, b):
 return a + b

print('结果是:', add(4, 5))