#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 2:15 PM
# @Author  : L
# @Email   : L862608263@163.com
# @File    : built_in_constants.py
# @Software: PyCharm

from Code.Tools.l_log import *

# 少量常量存在于内置命名空间中。 他们是：

# NOTE False

# 布尔类型的false值,帮False赋值是非法的并引发SyntaxError。
# False = 1 (SyntaxError: can't assign to keyword)

# NOTE True

# 布尔类型的true值,帮True赋值是非法的并引发SyntaxError。
# True = 1 (SyntaxError: can't assign to keyword)

# NOTE None

# NoneType类型的唯一值。

l_log(type(None))
l_log(None.__class__)
l_log(dir(None))

# None通常用于表示缺少值，因为默认参数未传递给函数
# 帮None赋值是非法的并引发SyntaxError。

# None = 1 (SyntaxError: can't assign to keyword)

# 方法里面如果没有返回, 默认返回None

def a():
    pass

l_log(a())

# NOTE NotImplemented

# NotImplemented 能被重新赋值（覆盖）。对它赋值，甚至改变属性名称， 不会产生 SyntaxError。
# 所以它不是一个真正的“真”常数。当然，我们应该永远不改变它。

# NotImplemented = 'do not'

# l_log(NotImplemented)

# NotImplemented 是个特殊值, 它能被二元特殊方法返回（比如__eq__()、__lt__()、__add__()、__rsub__()等,
# 表明某个类型没有像其他类型那样实现这些操作。
# 同样，它或许会被原地处理（in place）的二元特殊方法返回（比如__imul__()、__iand__()等）。
# 还有，它的实际值为True：

l_log(bool(NotImplemented))

# 以下通过个小例子, 来说明NotImplemented的作用

class A(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, A):
            print('Comparing an A with an A')
            return other.value == self.value
        if isinstance(other, B):
            print('Comparing an A with a B')
            return other.value == self.value
        print('Could not compare A with the other class')
        return NotImplemented


class B(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, B):
            print('Comparing a B with another B')
            return other.value == self.value
        print('Could not compare B with the other class')
        return NotImplemented


a1 = A(1)
b1 = B(1)

# 我们现在可以实验下对于 __eq__() 不同的调用，看看发生了什么。作为提醒，在Python中，a == b会调用a.__eq__(b)：

print(a1 == a1)

print(b1 == b1)

# 现在，如果我们比较b1和a1（即调用b1.__eq__(a1)），我们会想要返回NotImplemented。

print(b1 == a1)

# b1.__eq__(a1)方法返回NotImplemented，这样会导致调用A中的__eq__()方法。
# 而且由于在A中的__eq__()定义了A和B之间的比较，所以就得到了正确的结果（True）。

# 这就是返回了NotImplemented的所做的。
# NotImplemented告诉运行时，应该让其他对象来完成某个操作。
# 在表达b1 == a1中，b1.__eq__(a1)返回了NotImplemented，这说明Python试着用a1.__eq__(b1)。
# 由于a1足够可以返回True，因此这个表达可以成功。
# 如果A中的__eq__()也返回NotImplemented，那么运行时会退化到使用内置的比较行为，即比较对象的标识符(在CPython中，是对象在内存中的地址).

# 如果在调用b1.__eq__(a1)时抛出NotImpementedError，而不进行处理，就会中断代码的执行。
# 而NotImplemented无法抛出，仅仅是用来进一步测试是否有其他方法可供调用。


# NOTE Ellipsis

# 与省略号文字“...”相同。
# 特殊值
# 主要与用户定义的容器数据类型的扩展切片语法结合使用。

# 这东西是一个单例

l_log(id(...), id(...))

l_log(...)
l_log(type(...))

# 切片 (Slicings) 用来选取一个序列的某个范围并返回，这个过程归根结底是一次函数调用。
# 如lst[1:3]这样的切片操作会把slice(1,3,None)作为参数，传入__getitem__(self, key)这个方法中，
# 另外字典类型取值时a[k]实际上也是使用了这个__getitem__(self, key)方法。

# 那么可以通过修改这个东西来强行实现递推序列之类的玩意了。

# class Mogic(object):
#     def __getitem__(self, key):
#         if len(key) == 3 and key[2] is Ellipsis:
#             d = key[1] - key[0]
#             r = key[0]
#             while True:
#                 yield r
#                 r += d
#
# ap = Mogic()    # arithmetic progression
#
# import time
#
# for i in ap[1, 3, ...]:
#     print(i)         # caution: infinity loop here
#     time.sleep(1)    # slow down output


# 在输入提示里面使用

from typing import Callable

# 在类型提示中使用 Callable，不确定参数签名时，可以用 Ellipsis 占位。
def foo() -> Callable[..., int]:
    return lambda x: 1

l_log(foo())

# 使用 Tuple 时返回不定长的 tuple，用 Ellipsis 进行指定。

from typing import Tuple


def bar() -> Tuple[int, ...]:
    return 1, 2, 3


def buzz() -> Tuple[int, ...]:
    return 1, 2, 3, 4

l_log(buzz())

# 或者是在以.pyi结尾的文件即 stub files 中，声明一个变量并标记它的类型，而且不想给它初始值时使用。

from typing import IO

stream = ...  # type: IO[str]

l_log(stream)

# NOTE __debug__

# 如果Python未使用-O选项启动，则此常量为true。 另请参见断言语句。
# None，False，True和__debug__不能重新分配（对它们的赋值，即使作为属性名称，引发SyntaxError），因此它们可以被认为是“真正的”常量。

# NOTE 由site模块(初始化期间会自动导入该模块)添加的常量

# site模块（在启动期间自动导入，除非给出-S命令行选项）将向内置命名空间添加几个常量。 它们对交互式解释器shell很有用，不应在程序中使用。

