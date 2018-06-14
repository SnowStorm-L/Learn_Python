#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 PM2:28
# @Author  : L
# @Email   : L862608263@163.com
# @File    : lambda.py
# @Software: PyCharm


def defaultfunction(x):
    return 2 * x + 1


# 前面是原函数的参数 后面是返回值
# 这是个匿名函数

# 其实lambda不应该以以下2个例子使用
# 拿一个lambda赋值给lambdafunction 其实就相当于 def lambdafunction

lambdafunction = lambda x: 2 * x + 1

print(lambdafunction(5))

add = lambda x, y: x + y

print(add(4, 3))


# lambda的真正用途

# 先说说filter这个内置函数
#
# filter(function or None, iterable) --> filter object
#  |
#  |  Return an iterator yielding those items of iterable for which function(item)
#  |  is true. If function is None, return the items that are true.
#  返回一个迭代器，产生那些函数（item）为true的iterable项。 如果函数为None，则返回true的项目。

# [1, True]
print(list(filter(None, [1, 0, False, True])))

# 这里filter的第一个参数function就可以使用lambda
# 例如以下例子

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print(list(filter(lambda x: x % 3 == 0, foo)))

# 以下是不用lambda的原始方法


def functionname(x):
    return x % 3 == 0


print(list(filter(functionname, foo)))
# [18, 9, 24, 12, 27]

# map内置函数也可以使用lambda

print(list(map(lambda x: x * 2, range(10))))
