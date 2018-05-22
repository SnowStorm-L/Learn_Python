#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 PM4:03
# @Author  : L
# @Email   : L862608263@163.com
# @File    : magic_method.py
# @Software: PyCharm


# 据说，Python 的对象天生拥有一些神奇的方法，它们总被双下划线所包围，他们是面向对象的 Python 的一切。
# 他们是可以给你的类增加魔力的特殊方法，如果你的对象实现（重载）了这些方法中的某一个，那么这个方法就会在特殊的情况下被 Python 所调用，
# 你可以定义自己想要的行为，而这一切都是自动发生的。


# 基本的魔法方法

#  __new__(cls, *args, **kwargs):
# 1.__new__是在一个对象实例化的时候所调用的第一个方法
# 2.它的第一个参数是这个类，其他的参数是用来直接传递给__init__方法
# 3.__new__决定是否要使用该__init__方法，因为__new__可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果__new__没有返回实例对象，则__init__不会被调用
# 4.__new__主要是用于继承一个不可变的类型比如一个tuple或者string

#  __init__(self):
# 构造器，当一个实例被创建的时候调用的初始化方法

#  __del__(self):
# 析构器，当一个实例被销毁的时候调用的方法

#  __call__(self, *args, **kwargs):
# 允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)

#  __len__(self):
# 定义当被 len() 调用时的行为

#  __repr__(self):
# 定义当被 repr() 调用时的行为

#  __str__(self):
# 定义当被 str() 调用时的行为

#  __bytes__(self):
# 定义当被 bytes() 调用时的行为

#  __hash__(self):
# 定义当被 hash() 调用时的行为

#  __bool__(self):
# 定义当被 bool() 调用时的行为，应该返回 True 或 False

#  __format__(self, format_spec):
# 定义当被 format() 调用时的行为


# 有关属性

# __getattr__(self, item)
# 定义当用户试图获取一个不存在的属性时的行为
# 
# __getattribute__(self, item)
# 定义当该类的属性被访问时的行为
# 
# __setattr__(self, key, value)
# 定义当一个属性被设置时的行为
# 
# __delattr__(self, item)
# 定义当一个属性被删除时的行为
# 
# __dir__(self)
# 定义当dir()被调用时的行为
# 
# __get__(self, instance, owner)
# 定义当描述符的值被取得时的行为
# 
# __set__(self, instance, value)
# 定义当描述符的值被改变时的行为
# 
# __delete__(self, instance)
# 定义当描述符的值被删除时的行为


# 一个重写int的魔法方法的小例子

class Demo(int):

    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


print(Demo(5) + Demo(3))

