#!/usr/local/bin/python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 PM9:11
# @Author  : L
# @Email   : L862608263@163.com
# @File    : built_in_functions.py
# @Software: PyCharm

from Code.Tools.l_log import *

# Built-in Functions
# Python 内置方法
# Python 解释器有许多内置的函数和类型, 按字母排序介绍

# NOTE 1, abs(x)
# 返回一个数的绝对值。实参可以是整数或浮点数。如果实参是一个复数，返回它的模.

l_log(abs(-1))
l_log(abs(-1))
l_log(abs(-1.1))

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
l_log(z.real)  # 实部 获取
l_log(z.imag)  # 虚部 获取
l_log(z.conjugate())  # 输出该复数的共轭复数
l_log(abs(3 + 4j))

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

l_log("all empty_list", all(empty_list))
l_log("all demo_list", all(demo_list))
l_log("all demo_list_two", all(demo_list_two))

# NOTE 3, any(iterable) 楼上 NOTE 2 的亲戚

# 如果iterable的任何元素为 true, 则返回True 。如果 iterable 为空, 则返回False。
# 等效于:
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

l_log("any empty_list", any(empty_list))
l_log("any demo_list", any(demo_list))
l_log("any demo_list_two", any(demo_list_two))

# NOTE 4, ascii(object)

# 就像函数 repr(), 返回一个对象可打印的字符串, 但是 repr() 返回的字符串中非 ASCII 编码的字符，会使用 \x、\u 和 \U 来转义。
# 生成的字符串和 Python 2 的 repr() 返回的结果相似。

l_log(ascii(10), ascii(9000000), ascii('b\31'), ascii('0x\1000'), ascii('中文'))

# NOTE 5, bin(x)

# 将一个整数转变为一个前缀为“0b”的二进制字符串。
# 结果是一个合法的 Python 表达式。
# 如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数

l_log(bin(3), bin(-10))

# 如果需要前缀 "0b", 则可以使用下列任一方法。
l_log(format(14, '#b'), format(14, 'b'))
l_log(f'{14:#b}', f'{14:b}')

# NOTE 6, class bool([x])

# 返回一个布尔值, 即一个True或False。

# 使用标准真值测试程序(https://docs.python.org/3/library/stdtypes.html#truth 4.1条)转换x。
# 如果x为 false 或省略, 则返回False。否则它返回True。

# 在3.7 版中更改:x现在是仅限位置的参数。

# bool 类是 int 的子类别 (数字类型 --- int, float, complex)。
# 其他类不能继承自它。
# 它只有 False 和 True 两个实例（参见 Boolean Values）。

# 在 3.7 版更改: x 现在只能作为位置参数。

l_log(issubclass(bool, int))

l_log(bool(), bool(0), bool(1), bool(2))

# NOTE 7, breakpoint(*args: Any, **kws: Any) -> None

# 版本3.7中的新功能。

# 此函数会在调用时让你进入调试器中。

# 具体来说，它调用sys.breakpointhook（），直接传递args和kws。
# 默认情况下，sys.breakpointhook（）调用pdb.set_trace（）且没有参数.
# 在这种情况下，它纯粹是一个便利功能，因此您不必显式导入pdb且键入尽可能少的代码即可进入调试器
# 但是，sys.breakpointhook（）可以设置为其他一些函数，并被 breakpoint() 自动调用，以允许进入你想用的调试器。

# PDB(Python 的调试工具) 类似于iOS的lldb,Android的ADB

# NOTE 8, class bytearray([source[, encoding[, errors]]])

# 返回一个新的 bytes 数组。
# bytearray 类是一个可变序列，包含范围为 0 <= x < 256 的整数。
# 它有可变序列大部分常见的方法，见 Mutable Sequence Types 的描述；同时有 bytes 类型的大部分方法.
# 参见 Bytes and Bytearray Operations。

# 可选形参 source 可以用不同的方式来初始化数组：
# 1, 如果是一个 string，您必须提供 encoding 参数（errors 参数仍是可选的）；
# bytearray() 会使用 str.encode() 方法来将 string 转变成 bytes。

# 2, 如果是一个 integer，会初始化大小为该数字的数组，并使用 null 字节填充。

# 3, 如果是一个符合 buffer 接口的对象，该对象的只读 buffer 会用来初始化字节数组。

# 4, 如果是一个 iterable 可迭代对象，它的元素的范围必须是 0 <= x < 256 的整数，它会被用作数组的初始内容。

# 如果没有实参，则创建大小为 0 的数组。

b = bytearray()
l_log(b)

# NOTE 9, class bytes([source[, encoding[, errors]]])

# 返回一个新的“bytes”对象， 是一个不可变序列，包含范围为 0 <= x < 256 的整数。
# bytes 是 bytearray 的不可变版本 - 它有其中不改变序列的方法和相同的索引、切片操作。

# 因此，构造函数的实参和 bytearray() 相同。

# 字节对象还可以用字面值创建，参见 字符串和字节串字面值。

# 另见 二进制序列类型 --- bytes, bytearray, memoryview，字节对象 和 Bytes and Bytearray Operations。

# NOTE 10, callable(object)

# 如果实参 object 是可调用的，返回 True，否则返回 False。

# 如果返回真，调用仍可能会失败；但如果返回假，则调用 object 肯定会失败。
# 注意类是可调用的（调用类会返回一个新的实例）。如果实例的类有 __call__() 方法，则它是可调用。
# 可被调用指的是对象能否使用()括号的方法调用。

# 版本3.2中的新功能：此功能首先在Python 3.0中删除，然后在Python 3.2中恢复。

class A:
    pass


class B:  # 定义类B
    def __call__(self):
        l_log('instances are callable now.')


a = A()  # 调用类A
# 实例a不可调用

b = B()  # 调用类B
# 实例b是可调用对象

l_log(callable(B), callable(A), callable(a), callable(b))

# 调用实例b成功
b()

# NOTE 11, chr(i)

# 返回 Unicode 码位为整数 i 的字符的字符串格式。
# 例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。
# 这是 ord() 的逆函数。

# 实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。
# 如果 i 超过这个范围，会触发 ValueError 异常。

l_log(chr(97))
l_log(chr(8364))


# NOTE 12, @classmethod 类方法标志

# 一个类方法把类自己作为第一个实参，就像一个实例方法把实例自己作为第一个实参。
# 请用以下习惯来声明类方法:

class C:
    @classmethod
    def f(cls, arg1, arg2): ...


# @classmethod的构成 是一个函数装饰器
# 有关详细信息，请参阅函数定义中的函数定义说明。

# 可以在类上调用类方法（例如C.f（））或在一个实例上（例如C（）。f（））调用。
# 除了类之外，该实例被忽略。
# 如果为派生类调用类方法，则派生类对象将作为隐含的第一个参数传递。

# 类方法与C ++或Java静态方法不同。 如果需要，请参阅本节中的staticmethod()。
# 有关类方法的更多信息，请参阅标准类型层次结构中标准类型层次结构的文档。

# NOTE 13, compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

# 将 source 编译成代码或 AST 对象.  代码对象可以被 exec() 或 eval() 执行。
# source 可以是常规的字符串、字节字符串，或者 AST 对象。参见 ast 模块的文档了解如何使用 AST 对象。
# https://docs.python.org/3/library/ast.html#module-ast

# filename 实参需要是代码读取的文件名；如果代码不需要从文件中读取，可以传入一些可辨识的值（经常会使用 '<string>'）。

# mode 实参指定了编译代码必须用的模式。
# 如果 source 是语句序列，可以是 'exec'；如果是单一表达式，可以是 'eval'；如果是单个交互式语句，可以是 'single'。
# （在最后一种情况下，如果表达式执行结果不是  None 将会被打印出来。）


# 可选参数 flags 和 dont_inherit 控制在编译 source 时要用到哪个 future 语句。
# 如果两者都未提供（或都为零）则会使用调用 compile() 的代码中有效的 future 语句来编译代码。
# 如果给出了 flags 参数但没有 dont_inherit (或是为零) 则 flags 参数所指定的 以及那些无论如何都有效的 future 语句会被使用。
# 如果 dont_inherit 为一个非零整数，则只使用 flags 参数 -- 在调用外围有效的 future 语句将被忽略。

# Future 语句使用比特位来指定，多个语句可以通过按位或来指定。
# 具体特性的比特位可以通过 __future__ 模块中的 _Feature 类的实例的 compiler_flag 属性来获得。

# optimize 实参指定编译器的优化级别；默认值 -1 选择与解释器的 -O 选项相同的优化级别。
# 显式级别为 0 （没有优化；__debug__ 为真）、1 （断言被删除， __debug__ 为假）或 2 （文档字符串也被删除）。

# 如果编译的源码不合法，此函数会触发 SyntaxError 异常；如果源码包含 null 字节，则会触发 ValueError 异常。

# 如果要将 Python 代码解析为其 AST 表示形式, 请参见 ast.parse() .

# NOTE
# 在'single'或'eval'模式编译多行代码字符串时，输入必须以至少一个换行符结尾。 这使code模块更容易检测语句的完整性。

# WARNING
# 如果编译足够大或者足够复杂的字符串成 AST 对象时，Python 解释器会因为 Python AST 编译器的栈深度限制而奔溃。

# 在3.2 版中更改:允许使用 Windows 和 Mac 换行符。在'exec'模式下输入也不必再以换行符结束。添加了优化参数。
# 在 3.5 版更改: 之前 source 中包含 null 字节的话会触发 TypeError 异常。

for_in = "for i in range(0,10): print(i)"
for_in_compile = compile(for_in, '', 'exec')  # 编译为字节代码对象
exec(for_in_compile)

test = "3 * 4 + 5"
test_compile = compile(test, '', 'eval')
l_log(eval(test_compile))

# NOTE 14, class complex([real[, imag]])

# 返回值为 real + imag*1j 的复数，或将字符串或数字转换为复数。
# 如果第一个形参是字符串，则它被解释为一个复数，并且函数调用时必须没有第二个形参。
# 第二个形参不能是字符串。每个实参都可以是任意的数值类型（包括复数）。
# 如果省略了 imag，则默认值为零，构造函数会像 int 和 float 一样进行数值转换。如果两个实参都省略，则返回 0j。

# NOTE

# 当从字符串转换时，字符串在 + 或 - 的周围必须不能有空格。
# 例如 complex('1+2j') 是合法的，但 complex('1 + 2j') 会触发 ValueError 异常。

# 数字类型 --- int, float, complex 描述了复数类型。
# 在 3.6 版更改: 您可以使用下划线将代码文字中的数字进行分组。

l_log(complex(1, 2))
l_log(complex(1))
l_log(complex("1"))  # 当做字符串处理

# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
l_log(complex("1+2j"))


# 第一个参数为字符串，还添加第二个参数时会报错：
# print(complex('111', 2))  # TypeError: complex() can't take second arg if first is a string

# NOTE 15, delattr(object, name)

# setattr() 相关的函数。
# 实参是一个对象和一个字符串。
# 该字符串必须是对象的某个属性。
# 如果对象允许，该函数将删除指定的属性。
# 例如 delattr(x, 'foobar') 等价于 del x.foobar 。

class Coordinate:
    x = 10
    y = -5
    z = 0


point = Coordinate()
l_log('x = ', point.x)
l_log('y = ', point.y)
l_log('z = ', point.z)
delattr(Coordinate, 'z')
l_log('--删除 z 属性后--')
l_log('x = ', point.x)
l_log('y = ', point.y)
# 触发错误 AttributeError: 'Coordinate' object has no attribute 'z'
# print('z = ', point.z)

# NOTE 16, dict
"""
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
"""

# 创建一个新词典。 dict对象是一个字典类。
# 有关此类的文档，请参阅dict(https://docs.python.org/3/library/stdtypes.html#dict)
# 和Mapping Types - dict(https://docs.python.org/3/library/stdtypes.html#typesmapping)
# 其他容器类型，请参见内置的 list、set 和 tuple 类，以及 collections 模块。

# NOTE 17, dir([object])

# 如果没有实参，则返回当前本地作用域中的名称列表。
# 如果有实参，它会尝试返回该对象的有效属性列表。

# 如果对象有一个名为 __dir__() 的方法，那么该方法将被调用，并且必须返回一个属性列表。
# 这允许实现自定义 __getattr__() 或 __getattribute__() 函数的对象能够自定义 dir() 来报告它们的属性。

# 如果对象不提供 __dir__()，这个函数会尝试从对象已定义的 __dict__ 属性和类型对象收集信息。
# 结果列表并不总是完整的，如果对象有自定义 __getattr__()，那结果可能不准确。

# 默认的 dir() 机制对不同类型的对象行为不同，它会试图返回最相关而不是最全的信息：
# 1, 如果对象是模块对象，则列表包含模块的属性名称。
# 2, 如果对象是类型或类对象，则列表包含它们的属性名称，并且递归查找所有基类的属性。
# 3, 否则，列表包含对象的属性名称，它的类属性名称，并且递归查找它的类的所有基类的属性。

# 返回的列表按字母表排序。例如：

import struct

l_log(dir())  # 显示模块命名空间中的名称

l_log(dir(struct))  # 显示struct模块中的名称


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']


s = Shape()
l_log(dir(s))

# NOTE:

# 因为 dir() 主要是为了便于在交互式时使用，所以它会试图返回人们感兴趣的名字集合
# 而不是试图保证结果的严格性或一致性，它具体的行为也可能在不同版本之间改变。例如，当实参是一个类时，metaclass 的属性不包含在结果列表中。

# NOTE 18, divmod(a, b)

# 它将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数。
# 对于混合操作数类型，适用双目算术运算符的规则。
# 对于整数，结果和 (a // b, a % b) 一致
# 对于浮点数，结果是 (q, a % b) ，q 通常是 math.floor(a / b) 但可能会比 1 小。
# 在任何情况下， q * b + a % b 和 a 基本相等；如果 a % b 非零，它的符号和 b 一样，并且 0 <= abs(a % b) < abs(b) 。

# divmod(a,b)方法返回的是a//b（商）以及a%b(余数)，返回结果类型为tuple

divmod_test = divmod(9, 2)
l_log(divmod_test)
l_log(divmod_test[0])
l_log(divmod_test[1])

# NOTE 19, enumerate(iterable, start=0)

# 返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。
# enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

l_log(list(enumerate(seasons)))

l_log(list(enumerate(seasons, start=1)))


# enumerate的实现：

def custom_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


l_log(list(custom_enumerate(seasons)))

l_log(list(custom_enumerate(seasons, start=1)))

# NOTE 20, eval(expression, globals=None, locals=None)

# 实参是一个字符串，以及可选的 globals 和 locals。globals 实参必须是一个字典。locals 可以是任何映射对象。

# expression 参数会作为一个 Python 表达式（从技术上说是一个条件列表）被解析并求值，使用 globals 和 locals 字典作为全局和局部命名空间。
# 如果 globals 字典存在且不包含以 __builtins__ 为键的值，则会在解析 expression 之前插入以此为键的对内置模块 builtins 的字典的引用。
# 这意味着 expression 通常具有对标准 builtins 模块的完全访问权限且受限的环境会被传播。
# 如果省略 locals 字典则其默认值为 globals 字典。
# 如果两个字典同时省略，表达式会在 eval() 被调用的环境中执行。 返
# 回值为表达式求值的结果。 语法错误将作为异常被报告。 例如: demo 1

# 这个函数也可以用来执行任何代码对象（如 compile() 创建的）。
# 这种情况下，参数是代码对象，而不是字符串。
# 如果编译该对象时的 mode 实参是 'exec' 那么 eval() 返回值为 None 。

# 提示： exec() 函数支持动态执行语句。
# globals() 和 locals() 函数各自返回当前的全局和本地字典，因此您可以将它们传递给 eval() 或 exec() 来使用。

# demo 1
x = 1
l_log(eval('x+1'))

a = 1
g = {'a': 20}
l_log(eval("a+1", g))

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

l_log('locals x %d locals y %d globals x %d globals y %d' % (
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
l_log(z)

# eval有安全性问题,比如用户恶意输入就会获得当前目录文件

import os

l_log(eval("__import__('os').system('ls')"))

l_log('os' in globals())

l_log(os.system('whoami'))

# 怎么避免安全问题？
# １、自行写检查函数；
# ２、使用ast.literal_eval

# NOTE 21, exec(object[, globals[, locals]])

# 这个函数支持动态执行 Python 代码。
# object 必须是字符串或者代码对象。
# 如果是字符串，那么该字符串将被解析为一系列 Python 语句并执行（除非发生语法错误）。
# [1]如果是代码对象，它将被直接执行。在任何情况下，被执行的代码都需要和文件输入一样是有效的（见参考手册中关于文件输入的章节）。
# 请注意即使在传递给 exec() 函数的代码的上下文中，return 和 yield 语句也不能在函数定义之外使用。该函数返回值是 None 。

# 无论哪种情况，如果省略了可选参数，代码将在当前范围内执行。
# 如果提供了 globals 参数，就必须是字典类型，而且会被用作全局和本地变量。
# 如果同时提供了 globals 和 locals 参数，它们分别被用作全局和本地变量。
# 如果提供了 locals 参数，则它可以是任何映射型的对象。请记住在模块层级，全局和本地变量是相同的字典。
# 如果 exec 有两个不同的 globals 和 locals 对象，代码就像嵌入在类定义中一样执行。

# 如果 globals 字典不包含 __builtins__ 键值，则将为该键插入对内建 builtins 模块字典的引用。
# 因此，在将执行的代码传递给 exec() 之前，可以通过将自己的 __builtins__ 字典插入到 globals 中来控制可以使用哪些内置代码。

# NOTE
# 内置 globals() 和 locals() 函数各自返回当前的全局和本地字典，因此可以将它们传递给 exec() 的第二个和第三个实参。
# 默认情况下，locals 的行为如下面 locals() 函数描述的一样：不要试图改变默认的 locals 字典。
# 如果您想在 exec() 函数返回时知道代码对 locals 的变动，请明确地传递 locals 字典。

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

# 用 iterable 中函数 function 返回真的那些元素，构建一个新的迭代器。iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。
# 如果 function 是 None ，则会假设它是一个身份函数，即 iterable 中所有返回假的元素会被移除。

# 请注意， filter(function, iterable) 相当于一个生成器表达式，
# 当 function 不是 None 的时候为 (item for item in iterable if function(item))；
# function 是 None 的时候为 (item for item in iterable if item) 。

# 请参阅 itertools.filterfalse() 了解，只有 function 返回 false 时才选取 iterable 中元素的补充函数。

# 过滤出列表中的所有奇数：
def is_odd(n):
    return n % 2 == 1


new_list = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
l_log(list(new_list))

import math


# 过滤出1~100中平方根是整数的数：
def is_sqr(x):
    return math.sqrt(x) % 1 == 0


new_list_lambda = filter(lambda x: math.sqrt(x) % 1 == 0, range(1, 101))
new_list = filter(is_sqr, range(1, 101))
l_log(list(new_list))
l_log(list(new_list_lambda))

# NOTE 23, class float([x])

# 返回从数字或字符串 x 生成的浮点数。

# 如果实参是字符串，则它必须是包含十进制数字的字符串，字符串前面可以有符号，之前也可以有空格。
# 可选的符号有 '+' 和 '-' ； '+' 对创建的值没有影响。实参也可以是NaN（非数字）、正负无穷大的字符串。
# 确切地说，除去首尾的空格后，输入必须遵循以下语法：

"""
sign           ::=  "+" | "-"
infinity       ::=  "Infinity" | "inf"
nan            ::=  "nan"
numeric_value  ::=  floatnumber | infinity | nan
numeric_string ::=  [sign] numeric_value
"""

# 这里， floatnumber 是 Python 浮点数的字符串形式，详见 浮点数字面值。
# 字母大小写都可以，例如，“inf”、“Inf”、“INFINITY”、“iNfINity” 都可以表示正无穷大。

# 另一方面，如果实参是整数或浮点数，则返回具有相同值（在 Python 浮点精度范围内）的浮点数。
# 如果实参在 Python 浮点精度范围外，则会触发 OverflowError。

# 对于一般的 Python 对象 x ， float(x) 指派给 x.__float__() 。

# 如果没有实参，则返回 0.0 。

l_log(float('+1.23'), float('-12345\n'), float('1e-003'), float('+1E6'), float('-Infinity'))

# 数字类型 --- int, float, complex 描述了浮点类型。

# 在 3.6 版更改: 您可以使用下划线将代码文字中的数字进行分组。

# 在 3.7 版更改: x 现在只能作为位置参数。

# NOTE 24, format(value[, format_spec])

# 将 value 转换为 format_spec 控制的“格式化”表示。
# format_spec 的解释取决于 value 实参的类型，但是大多数内置类型使用标准格式化语法：Format Specification Mini-Language。

# 默认的 format_spec 是一个空字符串，它通常和调用 str(value) 的结果相同。

# 调用 format(value, format_spec) 会转换成 type(value).__format__(value, format_spec) ，
# 所以实例字典中的 __format__() 方法将不会调用。
# 如果搜索到 object 有这个方法但 format_spec 不为空，format_spec 或返回值不是字符串，会触发 TypeError 异常。

# 在 3.4 版更改: 当 format_spec 不是空字符串时， object().__format__(format_spec) 会触发 TypeError。

# NOTE 25, class frozenset([iterable])

# 返回一个新的 frozenset 对象，它包含可选参数 iterable 中的元素。
# frozenset 是一个内置的类。
# 有关此类的文档，请参阅 frozenset 和 集合类型 --- set, frozenset。

# 请参阅内建的 set、list、tuple 和 dict 类，以及 collections 模块来了解其它的容器。

# NOTE 26, getattr(object, name[, default])

# 返回对象命名属性的值。name 必须是字符串。
# 如果该字符串是对象的属性之一，则返回该属性的值。
# 例如， getattr(x, 'foobar') 等同于 x.foobar。
# 如果指定的属性不存在，且提供了 default 值，则返回它，否则触发 AttributeError。

class A(object):
    bar = 1


a = A()
getattr(a, 'bar')  # 获取属性 bar 值 1
# getattr(a, 'bar2')  # 属性 bar2 不存在，触发异常 AttributeError: 'A' object has no attribute 'bar2'
l_log(getattr(a, 'bar2', 3))  # 属性 bar2 不存在，但设置了默认值 3

# NOTE 27, globals()

# 返回表示当前全局符号表的字典。这总是当前模块的字典（在函数或方法中，不是调用它的模块，而是定义它的模块）。

# NOTE 28, hasattr(object, name)

# 该实参是一个对象和一个字符串。
# 如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。
# (此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）

# NOTE 29, hash(object)

# 返回该对象的哈希值（如果它有的话）。哈希值是整数。
# 它们在字典查找元素时用来快速比较字典的键。相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。

# 注意
# 如果对象实现了自己的 __hash__() 方法，请注意，hash() 根据机器的字长来截断返回值。另请参阅 __hash__()。

# NOTE 30, help([object)

# 启动内置的帮助系统（此函数主要在交互式中使用）。
# 如果没有实参，解释器控制台里会启动交互式帮助系统。
# 如果实参是一个字符串，则在模块、函数、类、方法、关键字或文档主题中搜索该字符串，并在控制台上打印帮助信息。
# 如果实参是其他任意对象，则会生成该对象的帮助页。

# 请注意如果在函数的形参列表中出现了斜杠 (/)，则它在发起调用 help() 的时候意味着斜杠之前的均为仅限位置形参。
# 更多相关信息，请参阅 有关仅限位置形参的 FAQ 条目。

# 该函数通过 site 模块加入到内置命名空间。

# 在 3.4 版更改: pydoc 和 inspect 的变更使得可调用对象的签名信息更加全面和一致。

help(float)

# NOTE 31, hex(x)

# 将整数转换为以“0x”为前缀的小写十六进制字符串。
# 如果 x 不是 Python int 对象，则必须定义返回整数的 __index__() 方法。

# 一些例子:
l_log(hex(255), hex(-42))

# 如果要将整数转换为大写或小写的十六进制字符串，并可选择有无“0x”前缀，则可以使用如下方法：
l_log('%#x' % 255, '%x' % 255, '%X' % 255)
l_log(format(255, '#x'), format(255, 'x'), format(255, 'X'))
l_log(f'{255:#x}', f'{255:x}', f'{255:X}')

# 另见 format() 获取更多信息。

# 另请参阅 int() 将十六进制字符串转换为以 16 为基数的整数。

# 注意
# 如果要获取浮点数的十六进制字符串形式，请使用 float.hex() 方法。

# NOTE 32, id(object)

# 返回对象的“标识值”。
# 该值是一个整数，在此对象的生命周期中保证是唯一且恒定的。两个生命期不重叠的对象可能具有相同的 id() 值。

# CPython实现细节：这是内存中对象的地址。

# NOTE 33, input([prompt])

# 如果存在 prompt 实参，则将其写入标准输出，末尾不带换行符。
# 接下来，该函数从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回。
# 当读取到 EOF 时，则触发 EOFError。例如:

# s = input('--> ')
# print(s)

# 如果加载了 readline 模块，input() 将使用它来提供复杂的行编辑和历史记录功能。

# NOTE 34, class int([x]), class int(x, base=10)

# 返回一个使用数字或字符串 x 生成的整数对象，或者没有实参的时候返回 0 。
# 如果 x 定义了 __int__()，int(x) 返回 x.__int__() 。
# 如果 x 定义了 __trunc__()，它返回 x.__trunc__() 。
# 对于浮点数，它向零舍入。

# 如果 x 不是数字，或者有 base 参数，x 必须是字符串、bytes、表示进制为 base 的 整数文字 的 bytearray 实例。
# 该文字前可以有 + 或 - （中间不能有空格），前后可以有空格。
# 一个进制为 n 的数字包含 0 到 n-1 的数，其中 a 到 z （或 A 到 Z ）表示 10 到 35。
# 默认的 base 为 10 ，允许的进制有 0、2-36。
# 2、8、16 进制的数字可以在代码中用 0b/0B 、 0o/0O 、 0x/0X 前缀来表示。
# 进制为 0 将安照代码的字面量来精确解释，最后的结果会是 2、8、10、16 进制中的一个。
# 所以 int('010', 0) 是非法的，但 int('010') 和 int('010', 8) 是合法的。

# 整数类型定义请参阅 数字类型 --- int, float, complex 。

# 在 3.4 版更改: 如果 base 不是 int 的实例，但 base 对象有 base.__index__ 方法，则会调用该方法来获取进制数。
# 以前的版本使用 base.__int__ 而不是 base.__index__。

# 在 3.6 版更改: 您可以使用下划线将代码文字中的数字进行分组。

# 在 3.7 版更改: x 现在只能作为位置参数。

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

# 如果 object 实参是 classinfo 实参的实例，或者是（直接、间接或 虚拟）子类的实例，则返回 true。
# 如果 object 不是给定类型的对象，函数始终返回 false。
# 如果 classinfo 是对象类型（或多个递归元组）的元组，如果 object 是其中的任何一个的实例则返回 true。
# 如果 classinfo 既不是类型，也不是类型元组或类型的递归元组，那么会触发 TypeError 异常。

a = "b"

l_log(isinstance(a, str))

# 参数classinfo为一个元组，则若对象类型与元组中类型名之一相同即返回True。
l_log(isinstance(a, (str, int, list)))


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

# 如果 class 是 classinfo 的子类（直接、间接或 虚拟 的），则返回 true。classinfo 可以是类对象的元组，此时 classinfo 中的每个元素都会被检查。
# 其他情况，会触发 TypeError 异常。

l_log(issubclass(B, A))
l_log(issubclass(B, (int, str)))


# NOTE 37, iter(object[, sentinel])

# 返回一个 iterator 对象。
# 根据是否存在第二个实参，第一个实参的解释是非常不同的。
# 如果没有第二个实参，object 必须是支持迭代协议（有 __iter__() 方法）的集合对象，或必须支持序列协议（有 __getitem__() 方法，且数字参数从 0 开始）。
# 如果它不支持这些协议，会触发 TypeError。
# 如果有第二个实参 sentinel，那么 object 必须是可调用的对象。
# 这种情况下生成的迭代器，每次迭代调用它的 __next__() 方法时都会不带实参地调用 object；
# 如果返回的结果是 sentinel 则触发 StopIteration，否则返回调用结果。

# 另请参见迭代器类型(Iterator Types)。

# 适合 iter() 的第二种形式的应用之一是构建块读取器。
# 例如，从二进制数据库文件中读取固定宽度的块，直至到达文件的末尾:

# with open('mydata.txt') as fp:
#     for line in iter(fp.readline, ''):
#         process_line(line)

# NOTE 38, len(s)

# 返回对象的长度（元素个数）。
# 实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）。

# NOTE 39, class list([iterable])

# 除了是函数，list 也是可变序列类型，详情请参阅 列表 和 序列类型 --- list, tuple, range。

# NOTE 40, locals()

# 更新并返回表示当前本地符号表的字典。在函数块而不是类块中调用 locals() 时会返回自由变量。

# NOTE
# 不要更改此字典的内容；更改不会影响解释器使用的局部变量或自由变量的值。

def runoob(arg):
    # 两个局部变量：arg、z
    z = 1
    print(locals())


runoob(4)
l_log(locals())

# NOTE 41, map(function, iterable, ...)

# 产生一个将 function 应用于迭代器中所有元素并返回结果的迭代器。
# 如果传递了额外的 iterable 实参，function 必须接受相同个数的实参，并使用所有迭代器中并行获取的元素。
# 当有多个迭代器时，最短的迭代器耗尽则整个迭代结束。如果函数的输入已经是元组实参，请参阅 itertools.starmap()。

# NOTE 42, max(iterable, *[, key, default]), max(arg1, arg2, *args[, key])

# 返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的。

# 如果只提供了一个位置参数，它必须是非空 iterable，返回可迭代对象中最大的元素；
# 如果提供了两个及以上的位置参数，则返回最大的位置参数。

# 有两个可选只能用关键字的实参。
# key 实参指定排序函数用的参数，如传给 list.sort() 的。
# default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。

# 如果有多个最大元素，则此函数将返回第一个找到的。
# 这和其他稳定排序工具如 sorted(iterable, key=keyfunc, reverse=True)[0] 和 heapq.nlargest(1, iterable, key=keyfunc) 保持一致。

# 3.4 新版功能: keyword-only 实参 default 。

# NOTE 43, memoryview(obj)

# 返回由给定实参创建的“内存视图”对象。
# 有关更多信息，请参阅 Memory Views(https://docs.python.org/3/library/stdtypes.html#typememoryview)

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
l_log(me.readonly)  # 只读的memoryview

mb = me[:2]  # 不会产生新的字符串

a = bytearray(b'aaaaaa')
me = memoryview(a)
l_log(me.readonly)  # 可写的memoryview
mb = me[:2]  # 不会会产生新的bytearray
mb[:2] = b'bb'  # 对mb的改动就是对me的改动

l_log(mb.tobytes())
'bb'

l_log(me.tobytes())
'bbaaaa'

# NOTE 44, min(iterable, *[, key, default]), min(arg1, arg2, *args[, key])

# 返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的。

# 如果只提供了一个位置参数，它必须是 iterable，返回可迭代对象中最小的元素；如果提供了两个及以上的位置参数，则返回最小的位置参数。

# 有两个可选只能用关键字的实参。
# key 实参指定排序函数用的参数，如传给 list.sort() 的。
# default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。

# 如果有多个最小元素，则此函数将返回第一个找到的。
# 这和其他稳定排序工具如 sorted(iterable, key=keyfunc)[0] 和 heapq.nsmallest(1, iterable, key=keyfunc) 保持一致。

# 3.4 新版功能: keyword-only 实参 default 。

# NOTE 45, next(iterator[, default])

# 通过调用 iterator 的 __next__() 方法获取下一个元素。
# 如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration。

# NOTE 46, class object

# 返回一个没有特征的新对象。
# object 是所有类的基类。
# 它具有所有 Python 类实例的通用方法。这个函数不接受任何实参。

# NOTE
# 由于 object 没有 __dict__，因此无法将任意属性赋给 object 的实例。

# NOTE 47, oct(x)

# 将一个整数转变为一个前缀为“0o”的八进制字符串。
# 结果是一个合法的 Python 表达式。
# 如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。一些例子

# demo
l_log(oct(8))
l_log(oct(-56))

# 如果要将整数转换为八进制字符串，或者使用前缀“0o”，则可以使用以下任一方法。

l_log('%#o' % 10, '%o' % 10)
l_log(format(10, '#o'), format(10, 'o'))
l_log(f'{10:#o}', f'{10:o}')

# 有关更多信息，另请参见format() https://docs.python.org/3/library/functions.html#format。

# NOTE 48, open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 打开 file 并返回对应的 file object。如果该文件不能打开，则触发 OSError。

# file 是一个 path-like object，表示将要打开的文件的路径（绝对路径或者当前工作目录的相对路径），也可以是要被封装的整数类型文件描述符。
# （如果是文件描述符，它会随着返回的 I/O 对象关闭而关闭，除非 closefd 被设为 False 。）

# mode 是一个可选字符串，用于指定打开文件的模式。
# 默认值是 'r' ，这意味着它以文本模式打开并读取。
# 其他常见模式有：写入 'w' （截断已经存在的文件）；
# 排它性创建 'x' ；
# 追加写 'a' （在 一些 Unix 系统上，无论当前的文件指针在什么位置，所有 写入都会追加到文件末尾）。
# 在文本模式，如果 encoding 没有指定，则根据平台来决定使用的编码：使用 locale.getpreferredencoding(False) 来获取本地编码。
# （要读取和写入原始字节，请使用二进制模式并不要指定 encoding。）可用的模式有：

"""
字符      意义
'r'     读取（默认）
'w'     写入，并先截断文件
'x'     排它性创建，如果文件已存在则失败
'a'     写入，如果文件存在则在末尾追加
'b'     二进制模式
't'     文本模式 (默认)
'+'     更新磁盘文件（读取并写入）
"""

# 默认的模式是 'r' （打开并读取文本，同 'rt' ）。
# 对于二进制写入， 'w+b' 模式打开并把文件截断成 0 字节； 'r+b' 则不会截断。

# 正如在 概述 中提到的，Python区分二进制和文本I/O。
# 以二进制模式打开的文件（包括 mode 参数中的 'b' ）返回的内容为 bytes`对象，不进行任何解码。
# 在文本模式下（默认情况下，或者在 *mode* 参数中包含 `'t'` ）时，
# 文件内容返回为 str ，首先使用指定的 encoding （如果给定）或者使用平台默认的的字节编码解码。

# 此外还允许使用一个模式字符 'U'，该字符已不再具有任何效果，并被视为已弃用。
# 之前它会在文本模式中启用 universal newlines，这在 Python 3.0 中成为默认行为。 请参阅 newline 形参的文档了解更多细节。

# NOTE
#  Python不依赖于底层操作系统的文本文件概念;所有处理都由Python本身完成，因此与平台无关。

# buffering 是一个可选的整数，用于设置缓冲策略。
# 传递0以切换缓冲关闭（仅允许在二进制模式下），
# 1选择行缓冲（仅在文本模式下可用），并且>1的整数以指示固定大小的块缓冲区的大小（以字节为单位）。如果没有给出 buffering
#  参数，则默认缓冲策略的工作方式如下:

# 1, 二进制文件以固定大小的块进行缓冲；使用启发式方法选择缓冲区的大小，尝试确定底层设备的“块大小”或使用 io.DEFAULT_BUFFER_SIZE。
# 在许多系统上，缓冲区的长度通常为4096或8192字节。

# 2, “交互式”文本文件（ isatty() 返回 True 的文件）使用行缓冲。其他文本文件使用上述策略用于二进制文件。

# encoding
# 是用于解码或编码文件的编码的名称。这应该只在文本模式下使用。

# 默认编码是依赖于平台的（无论locale.getpreferredencoding（）返回），但可以使用任何Python支持的 text encoding。
# 有关支持的编码列表请参阅codecs(https://docs.python.org/3/library/codecs.html#module-codecs)模块。

# errors
# 是一个可选的字符串参数，用于指定如何处理编码和解码错误 - 这不能在二进制模式下使用。

# 可以使用各种标准错误处理程序（列在 Error Handlers ），但是使用 codecs.register_error() 注册的任何错误处理名称也是有效的。

# 标准名称包括：
# 1, 如果存在编码错误，'strict' 会引发 ValueError 异常。 默认值 None 具有相同的效果。
# 2, 'ignore' 忽略错误。请注意，忽略编码错误可能会导致数据丢失。
# 3, 'replace' 会将替换标记（例如 '?' ）插入有错误数据的地方。
# 4, 'surrogateescape' 将表示任何不正确的字节作为Unicode专用区中的代码点，范围从U+DC80到U+DCFF。
# 当在写入数据时使用 surrogateescape 错误处理程序时，这些私有代码点将被转回到相同的字节中。这对于处理未知编码的文件很有用。

# 5, 只有在写入文件时才支持 'xmlcharrefreplace'。编码不支持的字符将替换为相应的XML字符引用 &#nnn;。
# 6, 'backslashreplace' 用Python的反向转义序列替换格式错误的数据。
# 7, 'namereplace' （也只在编写时支持）用 \N{...} 转义序列替换不支持的字符。

# newline 控制 universal newlines 模式如何生效（它仅适用于文本模式）。
# 它可以是 None，''，'\n'，'\r' 和 '\r\n'。

# 它的工作原理如下：

# 1, 从流中读取输入时，如果 newline 为 None，则启用通用换行模式。
# 输入中的行可以以 '\n'，'\r' 或 '\r\n' 结尾，这些行被翻译成 '\n' 在返回呼叫者之前。
# 如果它是 ''，则启用通用换行模式，但行结尾将返回给调用者未翻译。
# 如果它具有任何其他合法值，则输入行仅由给定字符串终止，并且行结尾将返回给未调用的调用者。

# 2, 将输出写入流时，如果 newline 为 None，则写入的任何 '\n' 字符都将转换为系统默认行分隔符 os.linesep。
# 如果 newline 是 '' 或 '\n'，则不进行翻译。如果 newline 是任何其他合法值，则写入的任何 '\n' 字符将被转换为给定的字符串。

# 如果 closefd 是 False 并且给出了文件描述符而不是文件名，那么当文件关闭时，底层文件描述符将保持打开状态。
# 如果给出文件名则 closefd 必须为 True （默认值），否则将引发错误。

# 可以通过传递可调用的 opener 来使用自定义开启器。
# 然后通过使用参数（ file，flags ）调用 opener 获得文件对象的基础文件描述符。
# opener 必须返回一个打开的文件描述符（使用 os.open as opener 时与传递 None 的效果相同）。

# 新创建的文件是不可继承的。

# 以下示例使用os.open（）函数的dir_fd参数打开相对于给定目录的文件：

# import os
#
# dir_fd = os.open('somedir', os.O_RDONLY)
#
#
# def opener(path, flags):
#     return os.open(path, flags, dir_fd=dir_fd)
#
#
# with open('spamspam.txt', 'w', opener=opener) as f:
#     print('This will be written to somedir/spamspam.txt', file=f)
# os.close(dir_fd)  # 不要泄漏文件描述符

# open() 函数所返回的 file object 类型取决于所用模式。
# 当使用 open() 以文本模式 ('w', 'r', 'wt', 'rt' 等) 打开文件时，它将返回 io.TextIOBase (特别是 io.TextIOWrapper) 的一个子类。
#  当使用缓冲以二进制模式打开文件时，返回的类是 io.BufferedIOBase 的一个子类。
# 具体的类会有多种：在只读的二进制模式下，它将返回 io.BufferedReader；
# 在写入二进制和追加二进制模式下，它将返回 io.BufferedWriter，而在读/写模式下，它将返回 io.BufferedRandom。
# 当禁用缓冲时，则会返回原始流，即 io.RawIOBase 的一个子类 io.FileIO。

# 另请参阅文件操作模块，例如 fileinput、io （声明了 open()）、os、os.path、tempfile 和 shutil。

# 在 3.3 版更改:
# 增加了 opener 形参。
# 增加了 'x' 模式。
# 过去触发的 IOError，现在是 OSError 的别名。
# 如果文件已存在但使用了排它性创建模式（ 'x' ），现在会触发 FileExistsError。
# 在 3.4 版更改:
# 文件现在禁止继承。
# Deprecated since version 3.4, will be removed in version 4.0: 'U' 模式。

# 在 3.5 版更改:
# 如果系统调用被中断，但信号处理程序没有触发异常，此函数现在会重试系统调用，而不是触发 InterruptedError 异常（原因详见 PEP 475）。
# 增加了 'namereplace' 错误处理接口。

# 在 3.6 版更改:
# 增加对实现了 os.PathLike 对象的支持。
# 在 Windows 上，打开一个控制台缓冲区将返回 io.RawIOBase 的子类，而不是 io.FileIO。

# NOTE 49, ord(c)

# 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。
# 例如 ord('a') 返回整数 97， ord('€') （欧元符合）返回 8364 。这是 chr() 的逆函数。

# NOTE 50, pow(x, y[, z])

l_log(pow(5, 2))

# 返回 x 的 y 次幂；如果 z 存在，则对 z 取余（比直接 pow(x, y) % z 计算更高效）。
# 两个参数形式的 pow(x, y) 等价于幂运算符： x**y。

# 参数必须为数值类型。 对于混用的操作数类型，则适用二元算术运算符的类型强制转换规则。
# 对于 int 操作数，结果具有与操作数相同的类型（转换后），除非第二个参数为负值；在这种情况下，所有参数将被转换为浮点数并输出浮点数结果。
# 例如，10**2 返回 100，但 10**-2 返回 0.01。
# 如果第二个参数为负值，则第三个参数必须省略。
# 如果存在 z，则 x 和 y 必须为整数类型，且 y 必须为非负数。

# NOTE 51, print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# 将 objects 打印到 file 指定的文本流，以 sep 分隔并在末尾加上 end。
# sep, end, file 和 flush 如果存在，它们必须以关键字参数的形式给出。

# 所有非关键字参数都会被转换为字符串，就像是执行了 str() 一样，并会被写入到流，以 sep 且在末尾加上 end。
# sep 和 end 都必须为字符串；它们也可以为 None，这意味着使用默认值。
# 如果没有给出 objects，则 print() 将只写入 end。

# file 参数必须是一个具有 write(string) 方法的对象；如果参数不存在或为 None，则将使用 sys.stdout。
# 由于要打印的参数会被转换为文本字符串，因此 print() 不能用于二进制模式的文件对象。 对于这些对象，应改用 file.write(...)。

# 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为真值，流会被强制刷新。
# 在 3.3 版更改: 增加了 flush 关键字参数。

# NOTE 52, class property(fget=None, fset=None, fdel=None, doc=None)

# 返回 property 属性。

# fget 是获取属性值的函数。
# fset 是用于设置属性值的函数。
# fdel 是用于删除属性值的函数。
# 并且 doc 为属性对象创建文档字符串。

# 一个典型的用法是定义一个托管属性 x:

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


# 如果 c 是 C 的实例，c.x 将调用getter，c.x = value 将调用setter， del c.x 将调用deleter。

# 如果给出，doc 将成为该 property 属性的文档字符串。

# 否则该 property 将拷贝 fget 的文档字符串（如果存在）。

# 这令使用 property() 作为 decorator 来创建只读的特征属性可以很容易地实现:

class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


# 以上 @property 装饰器会将 voltage() 方法转化为一个具有相同名称的只读属性的 "getter"，
# 并将 voltage 的文档字符串设置为 "Get the current voltage."

# 特征属性对象具有 getter, setter 以及 deleter 方法，它们可用作装饰器来创建该特征属性的副本，并将相应的访问函数设为所装饰的函数。
# 这最好是用一个例子来解释:

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


# 上述代码与第一个例子完全等价。 注意一定要给附加函数与原始的特征属性相同的名称 (在本例中为 x。)

# 返回的特征属性对象同样具有与构造器参数相对应的属性 fget, fset 和 fdel。

# 在 3.5 版更改: 特性属性对象的文档字符串现在是可写的。

# NOTE 53, range(stop)
# NOTE     range(start, stop[, step])

# 虽然被称为函数，但 range 实际上是一个不可变的序列类型，参见在 Ranges 与 序列类型 --- list, tuple, range 中的文档说明。

# NOTE 54, repr(object)

# 返回包含一个对象的可打印表示形式的字符串。
# 对于许多类型来说，该函数会尝试返回的字符串将会与该对象被传递给 eval() 时所生成的对象具有相同的值，
# 在其他情况下表示形式会是一个括在尖括号中的字符串，其中包含对象类型的名称与通常包括对象名称和地址的附加信息。
# 类可以通过定义 __repr__() 方法来控制此函数为它的实例所返回的内容。

l_log(repr([0, 1, 2, 3]))

# NOTE 55, reversed(seq)

# 返回一个反向的 iterator。
# seq 必须是一个具有__reversed__()方法的对象或者是支持该序列协议(具有从``0`` 开始的整数类型参数的 __len__() 方法和 __getitem__() 方法。

seq = [1, 2, 3]
l_log(reversed(seq))

# NOTE 56, round(number[, ndigits])

# 返回 number 舍入到小数点后 ndigits 位精度的值。 如果 ndigits 被省略或为 None，则返回最接近输入值的整数。

# 对于支持 round() 的内置类型，值会被舍入到最接近的 10 的负 ndigits 次幂的倍数；
# 如果与两个倍数的距离相等，则选择偶数 (因此，round(0.5) 和 round(-0.5) 均为 0 而 round(1.5) 为 2)。
# 任何整数值都可作为有效的 ndigits (正数、零或负数)。 如果 ndigits 被省略或为 None 则返回值将为整数。
# 否则返回值与 number 的类型相同。

# 对于一般的 Python 对象 number, round 将委托给 number.__round__。

# Note
# 对浮点数执行 round() 的行为可能会令人惊讶：例如，round(2.675, 2) 将给出 2.67 而不是期望的 2.68。
# 这不算是程序错误：这一结果是由于大多数十进制小数实际上都不能以浮点数精确地表示。

# 有关详细信息，请参阅浮点算术(https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues)：问题和限制。

# NOTE 57, class set([iterable])

# 返回一个新的 set 对象，可以选择带有从 iterable 获取的元素。 set 是一个内置类型。
# 请查看 set 和 集合类型 --- set, frozenset 获取关于这个类的文档。

# 有关其他容器请参看内置的 frozenset, list, tuple 和 dict 类，以及 collections 模块。

# NOTE 58, setattr(object, name, value)

# 此函数与 getattr() 两相对应。
# 其参数为一个对象、一个字符串和一个任意值。
# 字符串指定一个现有属性或者新增属性。
# 函数会将值赋给该属性，只要对象允许这种操作。 例如，setattr(x, 'foobar', 123) 等价于 x.foobar = 123。

# NOTE 59, class slice(stop)
# NOTE     class slice(start, stop[, step])

# 返回一个表示由 range(start, stop, step) 所指定索引集的 slice 对象。
# 其中 start 和 step 参数默认为 None。
# 切片对象具有仅会返回对应参数值（或其默认值）的只读数据属性 start, stop 和 step。 它们没有其他的显式功能；不过它们会被 NumPy 以及其他第三方扩展所使用。

# 切片对象也会在使用扩展索引语法时被生成。 例如: a[start:stop:step] 或 a[start:stop, i]。 请参阅 itertools.islice() 了解返回迭代器的一种替代版本。

# NOTE 60, sorted(iterable, *, key=None, reverse=False)

# 根据 iterable 中的项返回一个新的已排序列表。

# 具有两个可选参数，它们都必须指定为关键字参数。

# key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。
# 默认值为 None (直接比较元素)。

# reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。

# 使用 functools.cmp_to_key() 可将老式的 cmp 函数转换为 key 函数。

# 内置的 sorted() 确保是稳定的。
# 如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的 --- 这有利于进行多重排序（例如先按部门、再按薪级排序）。

# 有关排序示例和简要排序教程，请参阅排序方式。(https://docs.python.org/3/howto/sorting.html#sortinghowto)

# NOTE 61, @staticmethod

# 将方法转换为静态方法。

# 静态方法不会接收隐式的第一个参数。

# 要声明静态方法，请使用此语法

class C:
    @staticmethod
    def f(arg1, arg2): ...


# @staticmethod格式是一个函数装饰器(https://docs.python.org/3/glossary.html#term-decorator)
# - 有关详细信息，请参阅函数定义中的函数定义说明。
# 它可以在类（例如C.f() ）或实例（例如C().f() ）上调用。 除了类之外，该实例被忽略。

# Python中的静态方法与Java或C++中的静态方法类似。
# 另请参阅 classmethod() 以获取对创建备用类构造函数有用的变量。

# 像所有装饰器一样，也可以将staticmethod称为常规函数，并对其结果执行某些操作。
# 在需要从类主体引用函数并且您希望避免自动转换为实例方法的某些情况下，需要这样做。

# 对于这些情况，请使用此语法
class C:
    builtin_open = staticmethod(open)


# 有关静态方法的详细信息,请参阅标准类型层次结构中标准类型层次结构(https://docs.python.org/3/reference/datamodel.html#types)的文档

# NOTE 62, class str(object=''), class str(object=b'', encoding='utf-8', errors='strict')

# 返回一个 str 版本的 object 。有关详细信息，请参阅 str() 。
# str 是内置字符串 class 。更多关于字符串的信息查看 文本序列类型 --- str。

# 相关 看str.py

# NOTE 63, sum(iterable[, start])

# 从 start 开始自左向右对 iterable 中的项求和并返回总计值。
# start 默认为 0。
# iterable 的项通常为数字，开始值则不允许为字符串。

# 对某些用例来说，存在 sum() 的更好替代。
# 拼接字符串序列的更好更快方式是调用 ''.join(sequence)。
# 要以扩展精度对浮点值求和，请参阅 math.fsum()。
# 要拼接一系列可迭代对象，请考虑使用 itertools.chain()。

l_log(sum([0, 1, 2]))
l_log(sum((2, 3, 4), 1))  # 元组计算总和后再加 1  10


# NOTE 64, super([type[, object-or-type]])

# 返回一个代理对象，它会将方法调用委托给 type 指定的父类或兄弟类。
# 这对于访问已在类中被重载的继承方法很有用。
#  搜索顺序与 getattr() 所使用的相同，只是 type 指定的类型本身会被跳过。

# type 的 __mro__ 属性列出了 getattr() 和 super() 所使用的方法解析顺序。
# 该属性是动态的，可以在继承层级结构更新的时候任意改变。

# 如果省略第二个参数，则返回的超类对象是未绑定的。
# 如果第二个参数为一个对象，则 isinstance(obj, type) 必须为真值。
# 如果第二个参数为一个类型，则 issubclass(type2, type) 必须为真值（这适用于类方法）。

# super有两个典型的用例。
# 在具有单继承的类层级结构中，super 可用来引用父类而不必显式地指定它们的名称，从而令代码更易维护。
# 这种用法与其他编程语言中 super 的用法非常相似。

# 第二个用例是在动态执行环境中支持协作多重继承。
# 此用例为 Python 所独有，在静态编译语言或仅支持单继承的语言中是不存在的。
# 这使得实现“菱形图”成为可能，在这时会有多个基类实现相同的方法。
# 好的设计强制要求这种方法在每个情况下具有相同的调用签名（因为调用顺序是在运行时确定的，也因为该顺序要适应类层级结构的更改，
# 还因为该顺序可能包含在运行时之前未知的兄弟类）。

# 对于这两种用例，典型的超类调用如下所示：
class C(B):
    def method(self, arg):
        super().method(arg)
        # This does the same thing as:
        # super(C, self).method(arg)


# 请注意 super() 是作为显式加点属性查找的绑定过程的一部分来实现的，例如 super().__getitem__(name)。
# 它做到这一点是通过实现自己的 __getattribute__() 方法，这样就能以可预测的顺序搜索类，并且支持协作多重继承。
# 对应地，super() 在像 super()[name] 这样使用语句或操作符进行隐式查找时则未被定义。

# 还要注意的是，除了零个参数的形式以外，super() 并不限于在方法内部傅和。
# 两个参数的形式明确指定参数并进行相应的引用。
# 零个参数的形式仅适用于类定义内部，因为编译器需要填入必要的细节以正确地检索到被定义的类，还需要为普通访问当前实例。

# 有关如何使用super()设计合作类的实用建议，请参阅使用super()的指南。

# NOTE 65, tuple([iterable])

# 虽然被称为函数，但 tuple 实际上是一个不可变的序列类型，参见在 元组 与 序列类型 --- list, tuple, range 中的文档说明。
# 相关看 tuple.py

# NOTE 66, class type(object), class type(name, bases, dict)

# 传入一个参数时，返回 object 的类型。 返回值是一个 type 对象，通常与 object.__class__ 所返回的对象相同。

# 推荐使用 isinstance() 内置函数来检测对象的类型，因为它会考虑子类的情况。

# 传入三个参数时，返回一个新的 type 对象。
# 这在本质上是 class 语句的一种动态形式。
#  name 字符串即类名并且会成为 __name__ 属性；bases 元组列出基类并且会成为 __bases__ 属性；
# 而 dict 字典为包含类主体定义的命名空间并且会被复制到一个标准字典成为 __dict__ 属性。

# 例如，下面两条语句会创建相同的 type 对象:

class X:
    a = 1


X = type('X', (object,), dict(a=1))

# 也可以看看Type Objects(https://docs.python.org/3/library/stdtypes.html#bltin-type-objects)

# 在 3.6 版更改: type 的子类如果未重载 type.__new__，将不再能使用一个参数的形式来获取对象的类型。

# NOTE 67, vars([object])

# 返回模块、类、实例或任何其它具有 __dict__ 属性的对象的 __dict__ 属性。

# 模块和实例这样的对象具有可更新的 __dict__ 属性；
# 但是，其它对象的 __dict__ 属性可能会设为限制写入（例如，类会使用 types.MappingProxyType 来防止直接更新字典）。
# （例如，类使用types.MappingProxyType来防止直接字典更新）。

# 不带参数时，vars() 的行为类似 locals()。 请注意，locals 字典仅对于读取起作用，因为对 locals 字典的更新会被忽略。

# NOTE 68, zip(*iterables)

# 创建一个聚合了来自每个可迭代对象中的元素的迭代器。

# 返回一个元组的迭代器，其中的第 i 个元组包含来自每个参数序列或可迭代对象的第 i 个元素。
# 当所输入可迭代对象中最短的一个被耗尽时，迭代器将停止迭代。
# 当只有一个可迭代对象参数时，它将返回一个单元组的迭代器。

# 不带参数时，它将返回一个空迭代器。 相当于:

# def zip(*iterables):
#     # zip('ABCD', 'xy') --> Ax By
#     sentinel = object()
#     iterators = [iter(it) for it in iterables]
#     while iterators:
#         result = []
#         for it in iterators:
#             elem = next(it, sentinel)
#             if elem is sentinel:
#                 return
#             result.append(elem)
#         yield tuple(result)

# 函数会保证可迭代对象按从左至右的顺序被求值。
# 使得可以通过 zip(*[iter(s)]*n) 这样的惯用形式将一系列数据聚类为长度为 n 的分组。
# 这将重复 同样的 迭代器 n 次，以便每个输出的元组具有第 n 次调用该迭代器的结果。
# 它的作用效果就是将输入拆分为长度为 n 的数据块。

# 当你不用关心较长可迭代对象末尾不匹配的值时，则 zip() 只须使用长度不相等的输入即可。
# 如果那些值很重要，则应改用 itertools.zip_longest()。

# zip() 与 * 运算符相结合可以用来拆解一个列表:

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
l_log(list(zipped))

x2, y2 = zip(*zip(x, y))

l_log(x == list(x2) and y == list(y2))
l_log(x2)

# NOTE 69, __import__(name, globals=None, locals=None, fromlist=(), level=0)

#  与 importlib.import_module() 不同，这是一个日常 Python 编程中不需要用到的高级函数。

# 此函数会由 import 语句发起调用。
# 它可以被替换 (通过导入 builtins 模块并赋值给 builtins.__import__) 以便修改 import 语句的语义，
# 但是 强烈 不建议这样做，因为使用导入钩子 (参见 PEP 302)
# 通常更容易实现同样的目标，并且不会导致代码问题，因为许多代码都会假定所用的是默认实现。
# 同样也不建议直接使用 __import__() 而应该用 importlib.import_module()。

# 该函数会导入 name 模块，有可能使用给定的 globals 和 locals 来确定如何在包的上下文中解读名称。
# fromlist 给出了应该从由 name 指定的模块导入对象或子模块的名称。
# 标准实现完全不使用其 locals 参数，而仅使用 globals 参数来确定 import 语句的包上下文。

# level 指定是使用绝对还是相对导入。
# 0 (默认值) 意味着仅执行绝对导入。
#  level 为正数值表示相对于模块调用 __import__() 的目录，将要搜索的父目录层数 (详情参见 PEP 328)。

# 当 name 变量的形式为 package.module 时，通常将会返回最高层级的包（第一个点号之前的名称），而 不是 以 name 命名的模块。
# 但是，当给出了非空的 fromlist 参数时，则将返回以 name 命名的模块。

# 例如，语句 import spam 的结果将为与以下代码作用相同的字节码:
# spam = __import__('spam', globals(), locals(), [], 0)

# 语句 import spam.ham 的结果将为以下调用:
# spam = __import__('spam.ham', globals(), locals(), [], 0)

# 请注意在这里 __import__() 是如何返回顶层模块的，因为这是通过 import 语句被绑定到特定名称的对象。

# 另一方面，语句 from spam.ham import eggs, sausage as saus 的结果将为

# _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
# eggs = _temp.eggs
# saus = _temp.sausage

# 在这里， spam.ham 模块会由 __import__() 返回。 要导入的对象将从此对象中提取并赋值给它们对应的名称。

# 如果您只想按名称导入模块（可能在包中），请使用 importlib.import_module()

# 在 3.3 版更改: Negative values for level are no longer supported (which also changes the default value to 0).
