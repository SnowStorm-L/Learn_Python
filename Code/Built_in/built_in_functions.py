#!/usr/local/bin/python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 PM9:11
# @Author  : L
# @Email   : L862608263@163.com
# @File    : built_in_functions.py
# @Software: PyCharm

# Built-in Functions
# Python 内置方法
# Python 解释器有许多内置的函数和类型, 按字母排序介绍

# NOTE 1, abs(x)
# 返回数字的绝对值。参数可以是整数或浮点数字。如果参数是复数, 则返回其大小。


print(abs(-1))
print(abs(-1.1))
# 复数例子
# 复数: (mmp 数学是体育老师教的, 还是我铭记了有借有还的道理?)
#   我们把形如a+bi（a,b均为实数）的数称为复数，其中a称为实部，b称为虚部，i称为虚数单位(python 这里必须用 j 表示?)。
#
# 这个应该是计算复数的模, 而不是简单的3+4i=5，这是不存在等的关系的！因为一个是虚数，一个是实数。
# 应该是|3+4i|=5
# 复数的模计算方法是：|a+bi|=√(a^2+b^2)
# 所以，|3+4i|=√(3^2+4^2)=5
# 那么，|5+6i|=√61

# 实数范围内，负数没有平方根，所以-1的平方根是不存在的；
# 复数范围内，-1的平方根是正负i。

# 复数 z 或者表示 在x,y轴分别为3,4   复数就是->(长度为5  角度37°, 37°是勾股定理(3,4,5)形成的角度, 复数就是 5∠37或者写成 5 37°)
z = 3 + 4j
print(z.real)  # 实部 获取
print(z.imag)  # 虚部 获取
print(abs(3 + 4j))

# NOTE 2, all(iterable)

# 如果iterable的所有元素都为 true (或者 iterable 为空), 则返回True, 否则返回False。
# 等效于:
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

empty_list = list()
demo_list = list(range(1, 4))
demo_list_two = list(range(0, 3))

print("all empty_list", all(empty_list))
print("all demo_list", all(demo_list))
print("all demo_list_two", all(demo_list_two))

# NOTE 3, any(iterable) 楼上 NOTE 2 的亲戚

# 如果iterable的任何元素为 true, 则返回True 。如果 iterable 为空, 则返回False。
# 等效于:
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

print("any empty_list", any(empty_list))
print("any demo_list", any(demo_list))
print("any demo_list_two", any(demo_list_two))

# NOTE 4, ascii(object)

# 作为 repr(), 返回一个包含对象的可打印表示形式的字符串, 但在使用\x的 repr() 返回的字符串中转义非 ASCII 字符,\u或\U转义。
# 这将生成一个类似于 Python 2 中由 repr() 返回的字符串。

# 这个函数跟repr()函数一样，返回一个可打印的对象字符串方式表示。当遇到非ASCII码时，就会输出\x，\u或\U等字符来表示。
# 与Python 2版本号里的repr()是等效的函数。

print(ascii(10), ascii(9000000), ascii('b\31'), ascii('0x\1000'), ascii('中文'))

# NOTE 5, bin(x)

# 将整数数字转换为前缀为 "0b" 的二进制字符串。
# 结果是有效的 Python 表达式。如果x不是 Python int 对象, 它必须定义一个返回整数的 __index__() 方法。

print(bin(3), bin(-10))

# 如果需要前缀 "0b", 则可以使用下列任一方法。
print(format(14, '#b'), format(14, 'b'))
print(f'{14:#b}', f'{14:b}')

# NOTE 6, class bool([x])

# 返回一个布尔值, 即一个True或False。

# 使用标准真值测试程序(https://docs.python.org/3/library/stdtypes.html#truth 4.1条)转换x。
# 如果x为 false 或省略, 则返回False。否则它返回True。

# 在3.7 版中更改:x现在是仅限位置的参数。

# bool 类是 int 的子类别 (请参见数值类型-int、浮点、复数)。不能再创建子类了。它的唯一实例是False和True (请参见布尔值).
print(issubclass(bool, int))

print(bool(), bool(0), bool(1), bool(2))

# TODO 未完成 7, 8

# NOTE 7, breakpoint(*args: Any, **kws: Any) -> None

# 版本3.7中的新功能。

# 此函数将您放入调用站点的调试器中。

# 具体来说，它调用sys.breakpointhook（），直接传递args和kws。
# 默认情况下，sys.breakpointhook（）调用pdb.set_trace（）期望没有参数。
# 在这种情况下，它纯粹是一个便利功能，因此您不必显式导入pdb或输入尽可能多的代码来进入调试器。
# 但是，sys.breakpointhook（）可以设置为其他一些函数，breakpoint（）会自动调用它，允许你进入所选的调试器。

# NOTE 8, class bytearray(object)

