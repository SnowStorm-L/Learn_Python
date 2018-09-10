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


# WARNING 未完成 7, 8, 9

# NOTE 7, breakpoint(*args: Any, **kws: Any) -> None

# 版本3.7中的新功能。

# 此函数将您放入调用站点的调试器中。

# 具体来说，它调用sys.breakpointhook（），直接传递args和kws。
# 默认情况下，sys.breakpointhook（）调用pdb.set_trace（）期望没有参数。
# 在这种情况下，它纯粹是一个便利功能，因此您不必显式导入pdb或输入尽可能多的代码来进入调试器。
# 但是，sys.breakpointhook（）可以设置为其他一些函数，breakpoint（）会自动调用它，允许你进入所选的调试器。

# NOTE 8, class bytearray([source[, encoding[, errors]]])

# NOTE 9, class bytes([source[, encoding[, errors]]])

# NOTE 10, callable(object)

# 如果对象参数显示为可调用，则返回True，否则返回False。
# 如果返回true，则调用仍然可能失败，但如果为false，则调用对象将永远不会成功。
# 请注意，类是可调用的（调用类会返回一个新实例）; 如果实例的类具有__call __（）方法，则它们是可调用的。
# 可被调用指的是对象能否使用()括号的方法调用。

# 版本3.2中的新功能：此功能首先在Python 3.0中删除，然后在Python 3.2中恢复。

class A:
    pass


class B:  # 定义类B
    def __call__(self):
        print('instances are callable now.')


a = A()  # 调用类A
# 实例a不可调用

b = B()  # 调用类B
# 实例b是可调用对象

print(callable(B), callable(A), callable(a), callable(b))

# 调用实例b成功
b()

# NOTE 11, chr(i)

# 返回表示Unicode代码点为整数i的字符的字符串。
# 例如，chr（97）返回字符串'a'，而chr（8364）返回字符串'€'。
# 这是ord（）相反作用的函数。

print(chr(97))
print(chr(8364))


# NOTE 12, @classmethod 类方法标志

# 将方法转换为类方法。
# 类方法接收类作为隐式的第一个参数，就像实例方法接收实例一样。
# 要声明一个类方法，请使用此惯用语法：

class C:
    @classmethod
    def f(cls, arg1, arg2): ...

# @classmethod的构成 是一个函数装饰器
# 有关详细信息，请参阅函数定义中的函数定义说明。

# 它可以在类（ 例如C.f() ）或实例（ 例如C().f() ）上调用。
# 除了类之外，该实例被忽略。
# 如果为派生类调用类方法，则派生类对象将作为隐含的第一个参数传递。

# 类方法与C ++或Java静态方法不同。 如果需要，请参阅本节中的staticmethod()。
# 有关类方法的更多信息，请参阅标准类型层次结构中标准类型层次结构的文档。

# NOTE 13, compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

# 将源编译为代码或 AST 对象。 代码对象可以由 exec() 或 eval()执行。
# 源可以是普通字符串、字节字符串或 AST 对象。有关如何使用 ast 对象的信息, 请参阅 ast 模块文档。
# https://docs.python.org/3/library/ast.html#module-ast

# 文件名参数应提供从中读取代码的文件。如果没有从文件中读取 ('<string>' ), 请传递一些可识别的值。

# 模式参数指定必须编译的代码类型。
# 如果源由一组语句组成, 'eval' (如果包含单个表达式) 或'single' " (如果它由单个交互式语句组成),
# 则可以是'exec' (在后一种情况下, 将打印计算结果为非None的表达式语句)。

# 可选参数标志和dont_inherit控件, 将来的语句(https://docs.python.org/3/reference/simple_stmts.html#future)会影响源的编译。
# 如果两者都不存在 (或者两者都为零), 则代码将使用在调用 compile()的代码中生效的那些未来语句进行编译。
# 如果给出了flags参数, 并且dont_inherit不是 (或为零), 则除了将使用的语句之外, 还将使用由flags参数指定的未来声明
# 如果dont_inherit是非零整数, 则标志参数是它-将忽略在编译调用前后生效的未来语句。

# 未来的语句由位数指定, 可以按位 or 运算来指定多个语句。
# 指定给定功能所需的组标志可以被发现为 __future__ 模块_Feature实例上的compiler_flag属性。

# 参数优化指定编译器的优化级别;默认值-1根据给定的 -O 选项选择解释器的优化级别。
# 显式级别为0 (无优化;__debug__是真的), 1 (断言被删除, __debug__是假的) 或2 (单行也被删除)。

# 如果编译的源无效, 则此函数将引发 SyntaxError , 如果源包含 null 字节, 则 ValueError 。

# 如果要将 Python 代码解析为其 AST 表示形式, 请参见 ast.parse() .

# NOTE
# 在'single'或'eval'模式下使用多行代码编译字符串时, 输入必须至少由一个换行符终止。
# 这是为了便于在 code 模块中检测不完整和完整的语句.

# WARNING
# 由于 python 的 ast 编译器堆栈深度限制, 编译到 AST 对象时, 可能会使 python 解释程序与一个足够大/复杂的字符串碰撞.

# 在3.2 版中更改:允许使用 Windows 和 Mac 换行符。在'exec'模式下输入也不必再以换行符结束。添加了优化参数。
# 在3.5 版中更改:以前, 当源中遇到 null 字节时, TypeError 被引发。.
