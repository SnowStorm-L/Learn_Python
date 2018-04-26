#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 PM9:13
# @Author  : L
# @Email   : L862608263@163.com
# @File    : Variable.py
# @Software: PyCharm

# 局部变量(Local Variable)

# 全局变量(Global Variable)


def discounts(price, rate):
    """里面final_price就是局部变量, 出了这个方法(作用域),就挂了"""
    final_price = price * rate
    print('这里试图打印全局变量origin_price的值: ', origin_price)
    """
        origin_price = 50 // 定义不了,和上面的打印冲突了
        如果在函数内调用全局变量
        python会默认在函数内生成一个和全局变量同名的局部变量
        此时操作的只是局部变量
        
        如果非要在函数内修改全局变量,必须添加关键字global
        global origin_price
    """

    return final_price


# 下面这些是全局变量

origin_price = float(input('请输入原价: '))

rates = float(input('请输入折扣率: '))

new_price = discounts(origin_price, rates)

print('打折后价格是: ', new_price)
