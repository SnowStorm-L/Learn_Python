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


# 比较操作符

# __lt__(self, other)
# 定义小于号的行为：x < y 调用 x.__lt__(y)
#
# __le__(self, other)
# 定义小于等于号的行为：x <= y 调用 x.__le__(y)
#
# __eq__(self, other)
# 定义等于号的行为：x == y 调用 x.__eq__(y)
#
# __ne__(self, other)
# 定义不等号的行为：x != y 调用 x.__ne__(y)
#
# __gt__(self, other)
# 定义大于号的行为：x > y 调用 x.__gt__(y)
#
# __ge__(self, other)
# 定义大于等于号的行为：x >= y 调用 x.__ge__(y)


# 算数运算符

# __add__(self, other)
# 定义加法的行为：+
#
# __sub__(self, other)
# 定义减法的行为：-
#
# __mul__(self, other)
# 定义乘法的行为：*
#
# __truediv__(self, other)
# 定义真除法的行为：/
#
# __floordiv__(self, other)
# 定义整数除法的行为：//
#
# __mod__(self, other)
# 定义取模算法的行为：%
#
# __divmod__(self, other)
# 定义当被 divmod() 调用时的行为  divmod(a, b) 返回一个元祖: (a//b, a%b)
#
# __pow__(self, power, modulo=None)
# 定义当被 power() 调用或 ** 运算时的行为
#
# __lshift__(self, other)
# 定义按位左移位的行为：<<
#
# __rshift__(self, other)
# 定义按位右移位的行为：>>
#
# __and__(self, other)
# 定义按位与操作的行为：&
#
# __xor__(self, other)
# 定义按位异或操作的行为：^
#
# __or__(self, other)
# 定义按位或操作的行为：|


# 一个重写int的魔法方法的小例子

class Demo(int):

    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


print(Demo(5) + Demo(3))

# 反运算 （与上方相同，当左操作数不支持相应的操作时被调用）

# __radd__(self, other)	
# __rsub__(self, other)	
# __rmul__(self, other)	
# __rtruediv__(self, other)	
# __rfloordiv__(self, other)	
# __rmod__(self, other)	
# __rdivmod__(self, other)	
# __rpow__(self, other)	
# __rlshift__(self, other)	
# __rrshift__(self, other)	
# __rand__(self, other)	
# __rxor__(self, other)	
# __ror__(self, other)

# 例如: a + b
# a是主动, 但是如果a对象的add方法没有实现,或者不支持相应操作时
# python 就找到对象b的__radd__(self, other)方法


class Nint(int):

    def __radd__(self, other):
        print('__radd__方法执行了1-5')
        return int.__sub__(other, self)


a = Nint(3)
b = Nint(5)

print(a + b)

# 1找不到它的add方法,于是去找b, b执行的radd方法 返回sub结果
# 这里因为是b执行的方法,所以self是b  radd返回的sub参数要调换一下(other和self位置调换)
print(1 + b)


# 增量赋值运算

# __iadd__(self, other)	定义赋值加法的行为：+=
# __isub__(self, other)	定义赋值减法的行为：-=
# __imul__(self, other)	定义赋值乘法的行为：*=
# __itruediv__(self, other)	定义赋值真除法的行为：/=
# __ifloordiv__(self, other)	定义赋值整数除法的行为：//=
# __imod__(self, other)	定义赋值取模算法的行为：%=
# __ipow__(self, other[, modulo])	定义赋值幂运算的行为：**=
# __ilshift__(self, other)	定义赋值按位左移位的行为：<<=
# __irshift__(self, other)	定义赋值按位右移位的行为：>>=
# __iand__(self, other)	定义赋值按位与操作的行为：&=
# __ixor__(self, other)	定义赋值按位异或操作的行为：^=
# __ior__(self, other)	定义赋值按位或操作的行为：|=


# 一元操作符

# __pos__(self)	定义正号的行为：+x
# __neg__(self)	定义负号的行为：-x
# __abs__(self)	定义当被 abs() 调用时的行为
# __invert__(self)	定义按位求反的行为：~x


# 类型转换

# __complex__(self)
# 定义当被 complex() 调用时的行为（需要返回恰当的值）
#
# __int__(self)
# 定义当被 int() 调用时的行为（需要返回恰当的值）
#
# __float__(self)
# 定义当被 float() 调用时的行为（需要返回恰当的值）
#
# __round__(self, n=None)
# 定义当被 round() 调用时的行为（需要返回恰当的值）
#
# __index__(self)
# 1. 当对象是被应用在切片表达式中时，实现整形强制转换
# 2. 如果你定义了一个可能在切片时用到的定制的数值型,你应该定义 __index__
# 3. 如果 __index__ 被定义，则 __int__ 也需要被定义，且返回相同的值


# 上下文管理（with 语句）

# __enter__(self)
# 1. 定义当使用 with 语句时的初始化行为
# 2. __enter__ 的返回值被 with 语句的目标或者 as 后的名字绑定
#
# __exit__(self, exc_type, exc_value, exc_tb)
# 1. 定义当一个代码块被执行或者终止后上下文管理器应该做什么
# 2. 一般被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作


# 容器类型

# __len__(self)	定义当被 len()
# 调用时的行为（返回容器中元素的个数）
#
# __getitem__(self, key)
# 定义获取容器中指定元素的行为，相当于 self[key]
#
# __setitem__(self, key, value)
# 定义设置容器中指定元素的行为，相当于 self[key] = value
#
# __delitem__(self, key)
# 定义删除容器中指定元素的行为，相当于 del self[key]
#
# __iter__(self)
# 定义当迭代容器中的元素的行为
#
# __reversed__(self)
# 定义当被 reversed() 调用时的行为
#
# __contains__(self, item)
# 定义当使用成员测试运算符（in 或 not in）时的行为
