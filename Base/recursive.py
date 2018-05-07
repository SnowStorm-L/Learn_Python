#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 PM3:05
# @Author  : L
# @Email   : L862608263@163.com
# @File    : recursive.py
# @Software: PyCharm

import sys

# 设置递归最大深度
sys.setrecursionlimit(10000)

# 递归


def recursion():
    return recursion()

# 死循环
# RecursionError: maximum recursion depth exceeded
# 超过递归最大深度
# recursion()


def factorial(n):
    """阶乘例子"""
    return 1 if n == 1 else n * factorial(n - 1)
    # 非递归做法
    # result = n
    # for i in range(1, n):
    #     result *= i
    # return result

# 递归的流程
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1


print(factorial(5))

# 斐波那契数列  递归实现
# 1、1、2、3、5、8、13、21


def fibonaccisequence(n):
    return 1 if n < 3 else fibonaccisequence(n - 2) + fibonaccisequence(n - 1)


# 迭代实现

def iteration(n):

    if n < 3:
        return 1

    first = second = 1
    temp = i = 0

    while n - 2 > i:
        temp = first + second
        first = second
        second = temp
        i += 1
    return temp


# 汉诺塔游戏
# 3根柱子(x, y, z),仍以层数
def hanoitower(n, x='X', y='Y', z='Z'):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoitower(n-1, x, z, y)  # 将前n-1个盘子从x移动到y上
        print(x, '-->', z)  # 将最底下的最后一个盘子从x移动到z上
        hanoitower(n-1, y, x, z)  # 将y上的n-1个盘子移动到z上


print(hanoitower(3))


# *************************************************#
#      判断给定数的最大公约数，如果是素数，则打印         #
# *************************************************#
def show_max_factor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d最大的约数是%d' % (num, count))
            break
        count -= 1
    else:
        print('%d是素数！' % num)


number = int(input('请输入一个数：'))
show_max_factor(number)
