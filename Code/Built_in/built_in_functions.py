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
print(z.conjugate())  # 输出该复数的共轭复数
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

for_in = "for i in range(0,10): print(i)"
for_in_compile = compile(for_in, '', 'exec')  # 编译为字节代码对象
exec(for_in_compile)

test = "3 * 4 + 5"
test_compile = compile(test, '', 'eval')
print(eval(test_compile))

# NOTE 14, class complex([real[, imag]])

# 返回值为real + imag * 1j的复数或将字符串或数字转换为复数。
# 如果第一个参数是一个字符串，它将被解释为一个复数，并且必须在没有第二个参数的情况下调用该函数。
# 第二个参数永远不能是字符串。 每个参数可以是任何数字类型（包括复数）。
# 如果省略imag，则默认为零，构造函数用作int和float之类的数字转换。 如果省略两个参数，则返回0j。

# WARNING

# 从字符串转换时，字符串不得包含中心+或 - 运算符周围的空格。 例如，complex('1+2j'）很好，
# 但complex('1 + 2j'）引发ValueError。

# 复合类型在数值类型中描述, — int, float, complex.
# 版本3.6中已更改：允许使用下划线对数字进行分组，如代码文字中所示。

print(complex(1, 2))
print(complex(1))
print(complex("1"))  # 当做字符串处理

# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print(complex("1+2j"))


# 第一个参数为字符串，还添加第二个参数时会报错：
# print(complex('111', 2))  # TypeError: complex() can't take second arg if first is a string

# NOTE 15, delattr(object, name)

# 这是setattr()的亲戚。
# 参数是一个对象和一个字符串。
# 该字符串必须是对象属性之一的名称。
# 如果对象允许，该函数将删除命名属性。
# 例如，delattr（x，'foobar'）等同于del x.foobar。

class Coordinate:
    x = 10
    y = -5
    z = 0


point = Coordinate()
print('x = ', point.x)
print('y = ', point.y)
print('z = ', point.z)
delattr(Coordinate, 'z')
print('--删除 z 属性后--')
print('x = ', point.x)
print('y = ', point.y)
# 触发错误 AttributeError: 'Coordinate' object has no attribute 'z'
# print('z = ', point.z)

# NOTE 16, dict
"""
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
"""

# 创建一个新词典。 dict对象是字典类。
# 有关此类的文档，请参阅dict(https://docs.python.org/3/library/stdtypes.html#dict)
# 和Mapping Types - dict(https://docs.python.org/3/library/stdtypes.html#typesmapping)
# 对于其他容器，请参阅内置列表，set和tuple类以及collections模块。

# NOTE 17, dir([object])

# 如果没有参数，则返回当前本地范围中的名称列表。
# 使用参数，尝试返回该对象的有效属性列表。

# 如果对象具有名为 __dir__() 的方法，则将调用此方法，并且必须返回属性列表。
# 这允许实现自定义 __getattr__() 或 __getattribute__() 函数的对象自定义 dir() 报告其属性的方式。

# 如果对象未提供 __dir__() ，则该函数会尽力从对象的__dict__属性（如果已定义）及其类型对象中收集信息。
# 结果列表不一定完整，并且当对象具有自定义 __getattr__() 时可能不准确。

# 默认的 dir() 机制对不同类型的对象表现不同，因为它尝试生成最相关的信息，而不是完整的信息：
# 1, 如果对象是模块对象，则列表包含模块属性的名称。
# 2, 如果对象是类型或类对象，则列表包含其属性的名称，并递归地包含其基础的属性。
# 3, 否则，该列表包含对象的属性名称，其类的属性的名称，以及其类的基类的属性的递归。

# 结果列表按字母顺序排序。 例如：

import struct

print(dir())  # 显示模块命名空间中的名称

print(dir(struct))  # 显示struct模块中的名称


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']


s = Shape()
print(dir(s))

# NOTE:

# 因为 dir() 主要是为了方便在交互式提示中使用而提供的，所以它尝试提供一组有趣的名称，
# 而不是尝试提供严格或一致定义的名称集，并且其详细行为可能会在不同版本之间发生变化。
# 例如，当参数是类时，元类属性不在结果列表中。

# NOTE 18, divmod(a, b)

# 将两个（非复数）数作为参数，并在使用整数除法时返回由商和余数组成的一对数。
# 对于混合操作数类型，二进制算术运算符的规则适用。
# 对于整数，结果与（a // b，a％b）相同。
# 对于浮点数，结果为（q，a％b），其中q通常为math.floor（a / b），但可能比该值小1。
# 无论如何q * b + a％b非常接近a， 如果a％b非零，则其符号与b相同，并且 0 <= abs(a % b) < abs(b).

# NOTE 19, enumerate(iterable, start=0)

# 返回一个枚举对象。 iterable必须是序列，迭代器或支持迭代的其他对象。
# enumerate() 返回的迭代器的 __next__() 方法返回一个包含计数的元组（从start开始，默认为0）和迭代迭代得到的值。

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))


# enumerate的实现：

def custom_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


print(list(custom_enumerate(seasons)))

print(list(custom_enumerate(seasons, start=1)))

# NOTE 20, eval(expression, globals=None, locals=None)

# 参数是一个字符串和可选的全局变量和本地变量。 如果提供，globals必须是字典。 如果提供，则locals可以是任何映射对象。
# 表达式参数作为Python表达式（技术上讲，条件列表）被解析和评估，使用全局和本地字典作为全局和本地命名空间。
# 如果全局字典存在且不包含键__builtins__的值，则在解析表达式之前，会在该键下插入对内置模块内置字典的引用。
# 这意味着表达式通常具有对标准内置模块的完全访问权限，并且传播受限制的环境。
# 如果省略locals字典，则默认为globals字典。
# 如果省略两个字典，则表达式在调用 eval() 的环境中执行。
# 返回值是计算表达式的结果。
# 语法错误报告为异常。

# 此函数还可用于执行任意代码对象（例如由compile（）创建的代码对象）。
# 在这种情况下，传递代码对象而不是字符串。
# 如果代码对象已使用'exec'作为mode参数进行编译，则 eval() 的返回值将为None。

# 提示：exec（）函数支持动态执行语句。
# globals() 和 locals() 函数分别返回当前的全局和本地字典，这对于传递以供 eval() 或 exec() 使用可能很有用。
# 请参阅 ast.literal_eval() 以获取可以安全地评估包含仅包含文字的表达式的字符串的函数。

# demo 1
x = 1
print(eval('x+1'))

a = 1
g = {'a': 20}
print(eval("a+1", g))

# demo 2

x = 1
y = 1


def g():
    x = 2
    y = 2
    # 由于提供了globals()参数，那么首先应当找全局的x和y值，也就是都为1，那么显而易见，num的值也是2。
    # 如果注释掉该句，执行下面一句呢？结果为4
    # num = eval("x+y", globals())
    num = eval("x+y", globals(), locals())
    print("num", num)


g()

print('locals x %d locals y %d globals x %d globals y %d' % (
    locals()["x"], locals()["y"], globals()["x"], globals()["y"]))

# demo 3 locals()对象的值不能修改，globals()对象的值可以修改

z = 0


def f():
    z = 1
    print(locals())
    locals()["z"] = 2
    print(locals())


f()
globals()["z"] = 2
print(z)

# eval有安全性问题,比如用户恶意输入就会获得当前目录文件

import os

print(eval("__import__('os').system('ls')"))

print('os' in globals())

print(os.system('whoami'))

# 怎么避免安全问题？
# １、自行写检查函数；
# ２、使用ast.literal_eval

# NOTE 21, exec(object[, globals[, locals]])

# 此函数支持Python代码的动态执行。 object必须是字符串或代码对象。
# 如果它是一个字符串，则将该字符串解析为一组Python语句，然后执行该语句（除非发生语法错误）。如果它是一个代码对象，则只需执行它。
# 在所有情况下，执行的代码应该作为文件输入有效（请参见“参考手册”中的“文件输入”部分）。
# 请注意，即使在传递给exec（）函数的代码的上下文中，也不能在函数定义之外使用return和yield语句。
# 返回值为None。
# 在所有情况下，如果省略可选部分，则代码在当前范围内执行。
# 如果只提供全局变量，则它必须是字典，它将用于全局变量和局部变量。
# 如果给出全局变量和局部变量，则它们分别用于全局变量和局部变量。
# 如果提供，则locals可以是任何映射对象。
# 请记住，在模块级别，全局变量和本地变量是相同的字典。
# 如果exec获得两个单独的对象作为全局变量和局部变量，则代码将被执行，就好像它嵌入在类定义中一样。
# 如果全局字典不包含键__builtins__的值，则在该键下插入对内置模块内置字典的引用。
# 这样，您可以通过将自己的__builtins__字典插入到globals中，然后将其传递给 exec() 来控制已执行代码可用的内置函数。

# NOTE
# 内置函数 globals() 和 locals() 分别返回当前的全局和本地字典，这可能有助于传递用作 exec() 的第二个和第三个参数。
# 默认的locals的行为与下面的函数 locals() 相同：不应尝试修改默认的locals字典。
# 如果需要在函数 exec() 返回后查看代码对locals的影响，则传递显式的locals字典。

i = 2
j = 3
exec("ans = i + j")
# print("Answer is: ", ans)

# 在上个例子里面，ans变量并没有显式的定义，但仍然可以在print函数中调用。
# 这是exec语句执行了"ans = i + j"中的代码，定义了ans变量。

exec('print("Hello World")')

x = 10


def func():
    y = 20
    a = exec("x+y")
    print("a:", a)
    b = exec("x+y", {"x": 1, "y": 2})
    print("b:", b)
    c = exec("x+y", {"x": 1, "y": 2}, {"y": 3, "z": 4})
    print("c:", c)
    d = exec("print(x,y)")
    print("d:", d)


func()

x = 10
expr = """
z = 30
sum = x + y + z   #代码段
print(sum)
"""


def func():
    y = 20
    exec(expr)
    # 10 + 20 + 30
    exec(expr, {'x': 1, 'y': 2})
    # 30 + 1 + 2
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})  # 30+1+3，x是定义全局变量1，y是局部变量


func()


# NOTE 22, filter(function, iterable)

# 从iterable的元素中构造迭代器,函数返回 true。iterable可以是序列、支持迭代的容器或迭代器。
# 如果函数为None, 则假定标识函数为 false, 即删除所有iterable的元素。

# that filter(function, iterable) is equivalent to the generator
# expression (item for item in iterable if function(item))
# if function is not None and (item for item in iterable if item) if function is None.

# 有关函数返回false的迭代函数的补充函数，请参见itertools.filterfalse()。

# 过滤出列表中的所有奇数：
def is_odd(n):
    return n % 2 == 1


new_list = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(new_list))

import math


# 过滤出1~100中平方根是整数的数：
def is_sqr(x):
    return math.sqrt(x) % 1 == 0


new_list = filter(is_sqr, range(1, 101))
print(list(new_list))

# NOTE 23, class float([x])

# 返回由数字或字符串x构造的浮点数。
# 如果参数是一个字符串，它应该包含一个十进制数字，可选地以符号开头，并且可选地嵌入在空格中。
# 可选符号可以是“+”或“ - ”; “+”符号对产生的值没有影响。
# 参数也可以是表示NaN（非数字）或正或负无穷大的字符串。
# 更准确地说，在删除前导和尾随空格字符后，输入必须符合以下语法：

"""
sign           ::=  "+" | "-"
infinity       ::=  "Infinity" | "inf"
nan            ::=  "nan"
numeric_value  ::=  floatnumber | infinity | nan
numeric_string ::=  [sign] numeric_value
"""

# 这里floatnumber是Python浮点文字的形式,在浮点文字中描述。(https://docs.python.org/3/reference/lexical_analysis.html#floating)
# 案例并不重要，因此，例如，“inf”，“Inf”，“INFINITY”和“iNfINity”都是正无穷大的可接受拼写。
# 否则，如果参数是整数或浮点数，则返回具有相同值的浮点数（在Python的浮点精度内）。
# 如果参数超出Python float的范围，则会引发OverflowError。

# 对于一般的Python对象x，float（x）委托给x .__ float __（）。
# 如果没有给出参数，则返回0.0。

print(float('+1.23'), float('   -12345\n'), float('1e-003'), float('+1E6'), float('-Infinity'))


# float类型在Numeric Types中描述 - int，float，complex。

# 版本3.6中已更改：允许使用下划线对数字进行分组，如代码文字中所示。
# 在版本3.7中更改：x现在是仅位置参数。

# NOTE 24, format(value[, format_spec])

# 将值转换为“formatted”表示，由format_spec控制。
# format_spec的解释取决于value参数的类型，但是大多数内置类型都使用标准格式化语法：
# Format Specification Mini-Language。(https://docs.python.org/3/library/string.html#formatspec)

# 默认的format_spec是一个空字符串，通常与调用str（value）具有相同的效果。

# 对format（value，format_spec）的调用被转换为type（value）.__ format __（value，format_spec）
# 在搜索值的__format __（）方法时绕过实例字典。
# 如果方法搜索到达对象且format_spec为非空，或者format_spec或返回值不是字符串，则引发TypeError异常。
# 版本3.4中更改：object（）.__ format __（format_spec）如果format_spec不是空字符串，则引发TypeError。

# NOTE 25, class frozenset([iterable])

# 返回一个新的frozenset对象，可选地，从迭代中获取元素。
# frozenset 是一个内置的类。
# 有关此类的文档，请参阅frozenset和Set Types - set，frozenset。
# 对于其他容器，请参阅内置的set，list，tuple和dict类，以及collections模块。

# 具体例子看set.py

# NOTE 26, getattr(object, name[, default])

# 返回object的named属性的值。name必须是一个字符串。
# 如果字符串是对象属性之一的名称，则结果是该属性的值。
# 例如，getattr（x，'foobar'）等同于x.foobar。
# 如果named属性不存在，则返回default（如果提供），否则引发AttributeError。

class A(object):
    bar = 1


a = A()
getattr(a, 'bar')  # 获取属性 bar 值 1
# getattr(a, 'bar2')  # 属性 bar2 不存在，触发异常 AttributeError: 'A' object has no attribute 'bar2'
print(getattr(a, 'bar2', 3))  # 属性 bar2 不存在，但设置了默认值 3

# NOTE 27, globals()

# 返回表示当前全局符号表的字典。这始终是当前模块的字典 (在函数或方法内, 这是定义它的模块, 而不是调用它的模块)

# NOTE 28, hasattr(object, name)

# 参数是一个对象和一个字符串。如果字符串是对象属性之一的名称, 则结果为True , 否则为False 。
# (这是通过调用getattr(object, name)并查看它是否引发 AttributeError 来实现的。

# NOTE 29, hash(object)

# 返回对象的哈希值 (如果有)。哈希值为整数。它们用于在字典查找过程中快速比较字典键。
# 比较相等的数值具有相同的哈希值 (即使它们的类型不同, 1 和1.0 的情况也是如此)。

# 注意
# 对于具有自定义 __hash__() 方法的对象, 请注意, hash() 根据主机的位宽截断返回值。有关详细信息, 请参阅 __hash__() .

# NOTE 30, help([object)

# 调用内置帮助系统。
# 此函数用于交互式使用。如果未给出参数, 交互式帮助系统将在解释器控制台上启动。
# 如果参数是字符串, 则该字符串将被视为模块、函数、类、方法、关键字或文档主题的名称, 并在控制台上打印帮助页。
# 如果参数是任何其他类型的对象, 则会生成对象上的帮助页。

# 此函数由 site 模块添加到内置命名空间中

# 在3.4 版中更改:对 pydoc 和 inspect 的更改意味着 callables 的报告签名现在更加全面和一致。

help(float)

# NOTE 31, hex(x)

# 将整数数字转换为前缀为 "0x" 的小写十六进制字符串.
# 如果x不是 Python int 对象, 它必须定义一个返回整数的 __index__() 方法。
#
# 一些例子:
print(hex(255), hex(-42))

# 如果要将整数数字转换为带有前缀的大写或小写十六进制字符串, 可以使用下列任一方法
print('%#x' % 255, '%x' % 255, '%X' % 255)
print(format(255, '#x'), format(255, 'x'), format(255, 'X'))
print(f'{255:#x}', f'{255:x}', f'{255:X}')

# 有关详细信息, 请参阅 format() 。

# 另请参见int（），将十六进制字符串转换为使用16的基数的整数。

# 注意
# 若要获取浮点型的十六进制字符串表示形式, 请使用 float.hex() 方法.

# NOTE 32, id(object)

# 返回对象的 "标识"。
# 这是一个整数，在该生命周期内保证该对象是唯一且恒定的。
# 具有非重叠生命周期的两个对象可以具有相同的id()值。

# CPython实现细节：这是内存中对象的地址。

# NOTE 33, input([prompt])

# 如果存在prompt参数，则将其写入标准输出而不带尾随换行符。
# 然后该函数从输入中读取一行，将其转换为字符串（剥离尾部换行符），然后返回该行。
# 读取EOF时，会引发EOFError。

# s = input('--> ')
# print(s)

# 如果加载了readline模块，则input（）将使用它来提供精细的行编辑和历史记录功能。

# NOTE 34, class int([x]), class int(x, base=10)

# 返回由数字或字符串x构造的整数对象，如果没有给出参数，则返回0。
# 如果x定义__int__()，则int（x）返回x.__int__()。
# 如果x定义__trunc__()，则返回x.__trunc__()。
# 对于浮点数，这将截断为零。

# 如果x不是数字或者给定了base，则x必须是字符串，字节或bytearray实例，表示基数中的整数字面值。
# 可选地，文字可以在前面加+或 - （之间没有空格）并且用空格包围。
# base-n文字由数字0到n-1组成，a到z（或A到Z）的值为10到35。
# 默认基数为10.允许的值为0和2-36。 Base-2，-8和-16文字可以选择前缀为0b / 0B，0o / 0O或0x / 0X，与代码中的整数文字一样。
# 基数0表示完全解释为代码文字，因此实际基数为2,8,10或16，因此int（'010'，0）不合法，而int（'010'）是， 以及int（'010'，8）。

# 整数类型在数值类型中描述 - int，float，complex。

# 版本3.4中更改：如果base不是int的实例，并且基础对象具有base .__ index__方法，则调用该方法以获取基数的整数。
# 以前的版本使用base .__ int__而不是base .__ index__。

# 版本3.6中已更改：允许使用下划线对数字进行分组，如代码文字中所示。

# 在版本3.7中更改：x现在是仅位置参数。

"""
作用：

将一个数字或base类型的字符串转换成整数。

int(x=0)

int(x, base=10)，base缺省值为10，也就是说不指定base的值时，函数将x按十进制处理。

注：

1. x 可以是数字或字符串，但是base被赋值后 x 只能是字符串

2. x 作为字符串时必须是 base 类型，也就是说 x 变成数字时必须能用 base 进制表示
"""

# demo
# x 是数字的情况：

# int(3.14)            # 3
# int(2e2)             # 200
# int(100, 2)          # 出错，base 被赋值后函数只接收字符串

# x 是字符串的情况
# int('23', 16)      # 35
# int('Pythontab', 8)      # 出错，Pythontab不是个8进制数


# base 可取值范围是 2~36，囊括了所有的英文字母(不区分大小写)，十六进制中F表示15，
# 那么G将在二十进制中表示16，依此类推....Z在三十六进制中表示35

# int('FZ', 16)      # 出错，FZ不能用十六进制表示
# int('FZ', 36)      # 575

# 字符串 0x 可以出现在十六进制中，视作十六进制的符号，同理 0b 可以出现在二进制中，除此之外视作数字 0 和字母 x

# int('0x10', 16)  # 16，0x是十六进制的符号
# int('0x10', 17)  # 出错，'0x10'中的 x 被视作英文字母 x
# int('0x10', 36)  # 42804，36进制包含字母 x

# NOTE 35, isinstance(object, classinfo)

# 如果object参数是classinfo参数的实例，或者是（直接，间接或虚拟）子类的实例，则返回true。
# 如果object不是给定类型的对象，则该函数始终返回false。
# 如果classinfo是类型对象的元组（或递归，其他此类元组），则如果object是任何类型的实例，则返回true。
# 如果classinfo不是类型和类型元组的类型或元组，则会引发TypeError异常。

a = "b"

print(isinstance(a, str))

# 参数classinfo为一个元组，则若对象类型与元组中类型名之一相同即返回True。
print(isinstance(a, (str, int, list)))


#  isinstance()与type()的区别

# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# type() 不会认为子类是一种父类类型，不考虑继承关系。

class A:
    pass


class B(A):
    pass


isinstance(B(), A)  # returns True
type(B()) == A  # returns False

# NOTE 36, issubclass(class, classinfo)

# 如果class是classinfo的子类（直接，间接或虚拟），则返回true。
# 类被认为是其自身的子类。
# classinfo可以是类对象的元组，在这种情况下，将检查classinfo中的每个条目。
# 在任何其他情况下，都会引发TypeError异常。

print(issubclass(B, A))
print(issubclass(B, (int, str)))


# NOTE 37, iter(object[, sentinel])

# 返回一个迭代器对象。
# 根据第二个参数的存在，第一个参数的解释方式非常不同。
# 如果没有第二个参数，object必须是支持迭代协议（ __iter__() 方法）的集合对象，
# 或者它必须支持序列协议（ __getitem__() 方法，整数参数从0开始）。
# 如果它不支持这些协议中的任何一个，则引发TypeError。
# 如果给出第二个参数sentinel，则object必须是可调用对象。
# 在这种情况下创建的迭代器将为每个对__next __（）方法的调用调用没有参数的对象;
# 如果返回的值等于sentinel，则会引发StopIteration，否则返回该值。

# 另请参见迭代器类型(Iterator Types)。
# 第二种形式的 iter() 的一个有用的应用是读取文件的行直到达到某一行。
# 以下示例读取文件，直到readline（）方法返回空字符串：

# with open('mydata.txt') as fp:
#     for line in iter(fp.readline, ''):
#         process_line(line)

# NOTE 38, len(s)

# 返回对象的长度（项数）。
# 参数可以是序列（例如字符串，字节，元组，列表或范围）或集合（例如字典，集合或不可变集合）。

# NOTE 39, class list([iterable])

# 列表实际上是一种可变序列类型，而不是一个函数
# 如列表和序列类型中所述 - 列表，元组，范围。

# NOTE 40, locals()

# 更新并返回一个表示当前本地符号表的字典。当在函数块中调用, 而不是在类块中时, locals() 变量返回。

# NOTE
# 不应修改本词典的内容; 更改可能不会影响解释器使用的本地和自由变量的值.

def runoob(arg):
    # 两个局部变量：arg、z
    z = 1
    print(locals())


runoob(4)
print(locals())

# NOTE 41, map(function, iterable, ...)

# 返回一个迭代器，它将函数应用于每个iterable项，从而产生结果。
# 如果传递了其他可迭代参数，则函数必须采用那么多参数，并且并行地应用于所有迭代的项。
# 使用多个iterables时，迭代器会在最短的iterable耗尽时停止。
# 对于函数输入已经排列成参数元组的情况，请参阅itertools.starmap（）。
# https://docs.python.org/3/library/itertools.html#itertools.starmap

# NOTE 42, max(iterable, *[, key, default]), max(arg1, arg2, *args[, key])

# 返回可迭代中的最大项或两个或多个参数中的最大项。
# 如果提供了一个位置参数，则它应该是可迭代的。
# 返回iterable中的最大项。
# 如果提供了两个或多个位置参数，则返回最大的位置参数。

# 有两个可选的仅关键字参数。
# key参数指定一个单参数排序函数，就像list.sort（）一样。
# 如果提供的iterable为空，则default参数指定要返回的对象。
# 如果iterable为空并且未提供default，则引发ValueError。

# 如果多个项目是最大的，则该函数返回遇到的第一个项目。
# 这与其他排序稳定性保留工具一致，例如sorted（iterable，key = keyfunc，reverse = True）[0] 和
# heapq.nlargest（1，iterable，key = keyfunc）。

# 版本3.4中的新增功能：默认的仅限关键字参数。

# NOTE 43, memoryview(obj)

# 返回从给定参数创建的“内存视图”对象。
# 有关更多信息，请参阅内存视图(https://docs.python.org/3/library/stdtypes.html#typememoryview)

# 其中一个作用的demo

# 不使用memoryview

a = 'aaaaaa'
b = a[:2]  # 会产生新的字符串

a = bytearray(b'aaaaaa')
b = a[:2]  # 会产生新的bytearray
b[:2] = b'bb'  # 对b的改动不影响a

# 使用memoryview

a = b'aaaaaa'
me = memoryview(a)
print(me.readonly)  # 只读的memoryview

mb = me[:2]  # 不会产生新的字符串

a = bytearray(b'aaaaaa')
me = memoryview(a)
print(me.readonly)  # 可写的memoryview
mb = me[:2]  # 不会会产生新的bytearray
mb[:2] = b'bb'  # 对mb的改动就是对me的改动

print(mb.tobytes())
'bb'

print(me.tobytes())
'bbaaaa'

# NOTE 44, min(iterable, *[, key, default]), min(arg1, arg2, *args[, key])

# 返回可迭代中的最小项或两个或多个参数中的最小项。
# 如果提供了一个位置参数，则它应该是可迭代的。
# 返回iterable中的最小项。 如果提供了两个或多个位置参数，则返回最小的位置参数。

# 有两个可选的仅关键字参数。
# key参数指定一个单参数排序函数，就像list.sort（）一样。
# 如果提供的iterable为空，则default参数指定要返回的对象。
# 如果iterable为空并且未提供default，则引发ValueError。

# 如果多个项目是最小的，则该函数返回遇到的第一个项目。
# 这与其他排序稳定性保留工具（如sorted（iterable，key = keyfunc）[0]和
# heapq.nsmallest（1，iterable，key = keyfunc））一致。

# 版本3.4中的新增功能：默认的仅限关键字参数。

# NOTE 45, next(iterator[, default])

# 通过调用__next__() 方法从迭代器中检索下一个项。
# 如果给定default，则在迭代器耗尽时返回，否则引发StopIteration。

# NOTE 46, class object

# 返回一个新的无特征对象。
# object是所有类的基础。 它具有所有Python类实例共有的方法。
# 此函数不接受任何参数。

# NOTE
# 对象没有__dict__，因此您无法将任意属性分配给对象类的实例。

# NOTE 47, oct(x)

# 将整数转换为前缀为“0o”的八进制字符串。
# 结果是一个有效的Python表达式。

# 如果x不是Python int对象，则必须定义一个返回整数的__index__() 方法。

# demo
print(oct(8))
print(oct(-56))

# 如果要将整数转换为八进制字符串，或者使用前缀“0o”，则可以使用以下任一方法。

print('%#o' % 10, '%o' % 10)
print(format(10, '#o'), format(10, 'o'))
print(f'{10:#o}', f'{10:o}')

# 有关更多信息，另请参见format() https://docs.python.org/3/library/functions.html#format。

# NOTE 48, open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 打开文件并返回相应的文件对象。 如果无法打开文件，则会引发OSError。

# file是一个类似路径的对象，给出要打开的文件的路径名（绝对或相对于当前工作目录）或要包装的文件的整数文件描述符。
# （如果给出了文件描述符，则在关闭返回的I / O对象时将关闭它，除非将closefd设置为False。）

# mode是一个可选字符串，用于指定打开文件的模式。
# 默认为“r”，表示在文本模式下打开。
# 其他常见值是'w'用于写入（截断文件，如果它已经存在），
# 'x'用于独占创建，
# 'a'用于追加（在某些Unix系统上，意味着所有写入都附加到文件末尾） 目前寻求的位置）。

# 在文本模式下，如果未指定编码，则使用的编码与平台相关：调用locale.getpreferredencoding（False）以获取当前的语言环境编码。
# （对于读取和写入原始字节，请使用二进制模式并保留未指定的编码。）

# 可用的模式是：

"""
字符      意义
'r'     打开以进行读取 (默认)
'w'     打开写入，先截断文件
'x'     为独占创建打开, 如果文件已存在, 则失败
'a'     打开以进行写入, 如果该文件存在, 则追加到它的末尾
'b'     二进制模式
't'     文本模式 (默认)
'+'     打开磁盘文件进行更新 (读取和写入)
'U'     通用换行符模式 (已弃用)
"""

# 默认模式为'r' (打开以读取文本, 'rt'的同义词)。
# 对于二进制读写访问, 模式'w+b'打开并将文件截断为0字节。'r+b'打开文件而不截断。

# 正如概述中提到的, Python 区分二进制模式和文本 i/o 文件 (在模式参数中包括'b' ) 以 bytes返回内容。
# 没有任何解码的对象
# 在文本模式 (默认情况下, 或者在模式参数中包含't' ) 中, 文件的内容作为 str返回,
# 使用与平台相关的编码首先解码的字节或使用指定的编码(如果给定)。

# NOTE
# python 不依赖于底层操作系统对文本文件的概念; 所有的处理都是由 Python 本身完成的, 因此与平台无关.

# 缓冲(buffering)
# 是用于设置缓冲策略的可选整数。
# 通过0将缓冲关闭 (仅允许在二进制模式下)、1选择行缓冲 (仅在文本模式下可用) 和整数 > 1 表示固定大小的块缓冲区的大小 (以字节为单位)。

# 当没有给定缓冲参数时, 默认缓冲策略的工作原理如下:

# 1, 二进制文件以固定大小的区块进行缓冲;使用启发式方法来选择缓冲区的大小, 以确定底层设备的 "块大小" 并回到 io.DEFAULT_BUFFER_SIZE。
# 在许多系统上, 缓冲区通常为4096或8192字节长。

# 2, "交互式" 文本文件 ( isatty() 返回True的文件) 使用行缓冲。其他文本文件使用上面描述的用于二进制文件的策略。

# encoding
# 是用于解码或编码文件的编码的名称。这应该只在文本模式下使用。
# 默认编码取决于平台（无论locale.getpreferredencoding（）返回），但可以使用Python支持的任何文本编码。
# 请参阅编解码器模块(https://docs.python.org/3/library/codecs.html#module-codecs)以获取支持的编码列表。

# errors
# 是一个可选字符串，用于指定如何处理编码和解码错误 - 这不能在二进制模式下使用。
# 可以使用各种标准错误处理程序（在错误处理程序下列出），但已在codecs.register_error（）中注册的任何错误处理名称也有效。

# 标准名称包括：
# 1, 如果存在编码错误，则“strict”引发ValueError异常。 默认值None具有相同的效果。
# 2, 'ignore'忽略错误。 请注意，忽略编码错误可能会导致数据丢失。
# 3, 'replace'导致在有错误数据的地方插入替换标记（例如'？'）。
# 4, 'surrogateescape'将表示任何不正确的字节，如Unicode专用区中的代码点，范围从U + DC80到U + DCFF。
# 当在写入数据时使用surrogateescape错误处理程序时，这些私有代码点将被转回到相同的字节中。 这对于处理未知编码的文件很有用。
# 5, 只有在写入文件时才支持'xmlcharrefreplace'。 编码不支持的字符将替换为相应的XML字符引用＆＃nnn;。
# 6, 'backslashreplace'用Python的反向转义序列替换格式错误的数据。
# 7, 'namereplace'（也仅在编写时支持）用\ N {...}转义序列替换不支持的字符。

# newline
# 控制通用换行模式的工作方式（仅适用于文本模式）。
# 它可以是None，''，'\ n'，'\ r'和'\ r \ n'。

# 它的工作原理如下：

# 1, 从流中读取输入时，如果换行为“无”，则启用通用换行模式。
# 输入中的行可以以'\ n'，'\ r'或'\ r \ n'结尾，并且在返回给调用者之前将这些行转换为'\ n'。
# 如果是''，则启用通用换行模式，但行结尾将返回给调用者未翻译。
# 如果它具有任何其他合法值，则输入行仅由给定字符串终止，并且行结尾将返回给未调用的调用者。

# 2, 将输出写入流时，如果换行为None，则写入的任何“\ n”字符都将转换为系统默认行分隔符os.linesep。
# 如果换行符为''或'\ n'，则不会进行翻译。
# 如果换行符是任何其他合法值，则写入的任何“\ n”字符都将转换为给定的字符串。

# 如果closefd为False并且给出了文件描述符而不是文件名，则在关闭文件时，底层文件描述符将保持打开状态。
# 如果给出文件名，则closefd必须为True（默认值）否则将引发错误。

# 通过传递可调用的开启者可以使用自定义开启器。
# 然后通过使用（file，flags）调用opener来获取文件对象的基础文件描述符。

# opener
# 必须返回一个打开的文件描述符（传递os.open作为opener导致类似于传递None的功能）。

# FIXME open to be continue

# NOTE 49, ord(c)

# 给定表示一个Unicode字符的字符串，返回表示该字符的Unicode代码点的整数。
# 例如，ord（'a'）返回整数97，ord（'€'）（欧元符号）返回8364.这是chr（）的反转。

# NOTE 50, pow(x, y[, z])

print(pow(5, 2))


# modulo z（比pow（x，y）％z更有效地计算）。
# 两个参数形式pow（x，y）相当于使用幂运算符：x ** y。

# NOTE 51, print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# 将对象打印到文本流文件，以sep分隔，然后结束。
# sep，end，file和flush（如果存在）必须作为关键字参数给出。
# 所有非关键字参数都转换为str（）所做的字符串并写入流中，由sep分隔，然后是end。
# sep和end都必须是字符串; 它们也可以是None，这意味着使用默认值。
# 如果没有给出对象，print（）将只写入结束。

# file参数必须是带有write（string）方法的对象; 如果它不存在或None，将使用sys.stdout。
# 由于打印的参数转换为文本字符串，因此print（）不能与二进制模式文件对象一起使用。 对于这些，请改用file.write（...）。
# 输出是否缓冲通常由文件确定，但如果flush关键字参数为true，则强制刷新流。

# 版本3.3中已更改：添加了flush关键字参数。

# NOTE 52, class property(fget=None, fset=None, fdel=None, doc=None)

# fget是获取属性值的函数。
# fset是用于设置属性值的函数。
# fdel是用于删除属性值的函数。
# doc为该属性创建了一个docstring。

# 典型用法是定义托管属性x

class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


# 如果c是C的实例，c.x将调用getter，c.x = value将调用setter和del c.x删除器。
# 如果给定，doc将是property属性的docstring。
# 否则，该属性将复制fget的docstring（如果存在）。

# 这使得使用property（）作为装饰器可以轻松创建只读属性：

class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


# @property装饰器将voltage（）方法转换为具有相同名称的只读属性的“getter”，并将_voltage(电压)的docstring设置为“获取当前电压”。

# 属性对象具有可用作装饰器的getter，setter和deleter方法，这些方法创建属性的副本，并将相应的访问器函数设置为修饰函数。
# 最好用一个例子来解释：

class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


# 此代码与第一个示例完全等效。 请务必为其他函数指定与原始属性相同的名称（在本例中为x）。
# 返回的属性对象还具有与构造函数参数对应的属性fget，fset和fdel。

# 在版本3.5中更改：属性对象的文档字符串现在是可写的。

# NOTE 53, range(stop)
# NOTE     range(start, stop[, step])

# 范围实际上是一个不可变的序列类型，而不是一个函数，如范围和序列类型 - list，tuple，range中所述。

# NOTE 54, repr(object)

# 返回包含对象的可打印表示的字符串(返回一个对象的 string 格式)。
# 对于许多类型，此函数尝试返回一个字符串，该字符串在传递给eval（）时会产生具有相同值的对象，否则表示形式是一个用尖括号括起来的字符串，
# 它包含对象类型的名称 附加信息通常包括对象的名称和地址。

# 类可以通过定义__repr __（）方法来控制此函数为其实例返回的内容。

print(repr([0, 1, 2, 3]))

# NOTE 55, reversed(seq)

# 返回反序迭代器。
# seq必须是一个具有__reversed __（）方法的对象，或者支持序列协议（__len __（）方法和__getitem __（）方法，整数参数从0开始）。

# NOTE 56, round(number[, ndigits])

# 小数点后舍入到ndigits精度的返回数。
# 如果省略ndigits或者为None，则返回其输入的最接近的整数。

# 对于支持round（）的内置类型，值被舍入到10的最接近的倍数到幂减去ndigits;
# 如果两个倍数相等，则向均匀选择进行舍入（例如，round（0.5）和round（-0.5）均为0，round（1.5）为2）。
# 任何整数值对ndigits（正数，零或负数）有效。
# 如果省略ndigits或None，则返回值为整数。否则返回值与数字的类型相同。

# 对于一般的Python对象编号，将代理舍入为.__ round__。

# Note
# round（）对于浮点数的行为可能会令人惊讶：例如，round（2.675,2）给出2.67而不是预期的2.68。
# 这不是一个错误：这是因为大多数小数部分不能完全表示为浮点数。

# 有关详细信息，请参阅浮点算术(https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues)：问题和限制。

# NOTE 57, class set([iterable])

# 返回一个新的set对象，可选地包含从iterable中获取的元素。
# set是一个内置类。
# 有关此类的文档，请参阅set和Set Types - set，frozenset。
# 对于其他容器，请参阅内置的frozenset，list，tuple和dict类，以及collections模块。

# NOTE 58, setattr(object, name, value)

# 这是getattr（）的对应物。
# 参数是一个对象，一个字符串和一个任意值。
# 该字符串可以命名现有属性或新属性。
# 如果对象允许，该函数会将值分配给属性。
# 例如，setattr（x，'foobar'，123）等效于x.foobar = 123。

# NOTE 59, class slice(stop)
# NOTE     class slice(start, stop[, step])

# 返回一个切片对象，表示由range（start，stop，step）指定的索引集。
# start和step参数默认为None。
# Slice对象具有只读数据属性start，stop和step，它们只返回参数值（或它们的默认值）。
# 他们没有其他明确的功能;但是它们被Numerical Python和其他第三方扩展使用。 使用扩展索引语法时也会生成切片对象。
# 例如：a [start：stop：step]或[start：stop，i]。 有关返回迭代器的备用版本，请参阅itertools.islice（）。

# NOTE 60, sorted(iterable, *, key=None, reverse=False)

# 从iterable中的项返回一个新的排序列表。
# 有两个可选参数，必须指定为关键字参数。
# key指定一个参数的函数，该函数用于从每个列表元素中提取比较键：key = str.lower。默认值为None（直接比较元素）。

# reverse是一个布尔值。 如果设置为True，则列表元素将按照每个比较相反的方式进行排序。

# 使用functools.cmp_to_key（）将旧式cmp函数转换为键函数。

# 内置的sorted（）函数保证稳定。如果排序保证不更改比较相等的元素的相对顺序，则排序是稳定的 - 这有助于在多个过程中进行排序
# （例如，按部门排序，然后按工资等级排序）。

# 有关排序示例和简要排序教程，请参阅排序方式。(https://docs.python.org/3/howto/sorting.html#sortinghowto)
