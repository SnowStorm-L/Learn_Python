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


# 内嵌函数(函数嵌套)
# 内部函数的作用域都在外部函数之内

def fun1():
    print('fun1()正在被调用')

    def fun2():
        print('fun2()正在被调用')
    fun2()


fun1()


# 闭包(Closure)(函数式编程的重要语法结构)

# 如果在一个内部函数里,对外部作用域的变量进行引用(但不是在全局作用域的变量进行引用)
# 内部函数就会被认为是闭包


def external(x):
    # 1,对于external   internal就是一个内部函数
    def internal(y):
        # 2, internal对外部作用域(就是external的作用域)的变量(这里是x)进行引用
        # 达到1,2两点需求的话  就是闭包(internal是闭包)
        return x * y
    return internal


# 调用

call = external(8)

# <function external.<locals>.internal at 0x10f80e048>
print(call)
# <class 'function'>
print(type(call))

print(call(5))

print(external(8)(5))


def checkparams(fn):
    def wrapper(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return fn(a, b)
        logging.warning("variable 'a' and 'b' can't not be add")
        return
    return wrapper


# 语法糖写法  @函数名(这是个装饰器)
# 加了这个就不用 add = checkparams(add),可以直接使用add,这只是一种写法上的优化，解释器仍然会将它转化为add = checkParams(add)来执行
# @checkparams
def add(a, b):
    return a + b

# 调用方法1
# add = checkparams(add)
# add(3, 'test'))


# 调用方法2
print('结果是:', checkparams(add)(5, 8))


# 错误示范
# def fun1():
#     x = 5 # 这里被屏蔽起来了
#     def func2():
#         x *= x  # x被认为是局部变量
#         return x
#     return func2()
# local variable 'x' referenced before assignment
# 局部变量'x'不能在没有定义之前引用

# python3 之前是没有直接的解决方法的,只能通过以下的间接解决方法(容器类型,不是存放在栈里面,不会被屏蔽)

# def fun1():
#     x = [5]
#     def func2():
#         x[0] *= x[0]
#         return x[0]
#     return func2()
#
# print('结果~~~~~',fun1())


# python3 后 添加 nonlocal 关键字
# def fun1():
#     x = 5
#     def func2():
#         nonlocal x
#         x *= x
#         return x
#     return func2()


# LEGB法则
# LEGB就是用来规定命名空间查找顺序的规则

# LEGB含义解释：
# L-Local(function)；函数内的名字空间
# E-Enclosing function locals；外部嵌套函数的名字空间(例如closure)
# G-Global(module)；函数定义所在模块（文件）的名字空间
# B-Builtin(Python)；Python内置模块的名字空间

# Python的命名空间是一个字典，字典内保存了变量名称与对象之间的映射关系，因此，查找变量名就是在命名空间字典中查找键-值对。

# 官网文档 https://docs.python.org/3.4/tutorial/classes.html
# A namespace is a mapping from names to objects.
# 命名空间是从名称到对象的映射
# Most namespaces are currently implemented as Python dictionaries,
# 大多数命名空间当前是以 Python 字典的形式实现的,
# but that’s normally not noticeable in any way (except for performance), and it may change in the future.
# 但这通常不会以任何方式引人注目（除了性能）, 而且将来可能会发生变化.

# 由以下例子证明
class NameSpace:

    b = 5


# 打印就可以看到变量b=5的字典存储方式了
# 由于这是一种映射关系，所以，可以使用键-值的形式来表示，即{'b': 5}。
# 字典{name(str类型) : object(any类型)}
print(NameSpace.__dict__)


# 前面讲到，Python的命名空间是一个字典，字典内保存了变量名称与对象之间的映射关系，因此，查找变量名就是在命名空间字典中查找键-值对。
# Python有多个命名空间，因此，需要有规则来规定，按照怎样的顺序来查找命名空间，LEGB就是用来规定命名空间查找顺序的规则。

# LEGB规定了查找一个名称的顺序为：local-->enclosing function locals-->global-->builtin
# 在任何一层先找到了符合要求的变量名，则不再向更外层查找。
# 如果直到Builtin层仍然没有找到符合要求的变量，则抛出NameError异常。这就是变量名解析的：LEGB法则。


x = 1


def foo():

    x = 2

    def innerfoo():

        # x = 3
        # x = 3 属于函数内部命名空间，当被注释掉之后，函数innerfoo内部通过print x 使用x这个名称时，触发了名称查找动作。
        # 首先在Local命名空间查找，没有找到，然后到Enclosing function locals命名空间查找，查找成功，然后调用。

        print('locals ', x)

    innerfoo()

    print('enclosing function locals ', x)


foo()

print('global ', x)

