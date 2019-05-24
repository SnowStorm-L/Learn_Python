#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 3:03 PM
# @Author  : L
# @Email   : L862608263@163.com
# @File    : built_in_types.py
# @Software: PyCharm

from Code.Tools.l_log import *

# 内置类型

# 以下部分描述了解释器中内置的标准类型。

# 主要内置类型有数字、序列、映射、类、实例和异常。

# 有些多项集类是可变的。
# 它们用于添加、移除或重排其成员的方法将原地执行，并不返回特定的项，绝对不会返回多项集实例自身而是返回 None。

# 有些操作受多种对象类型的支持;特别地,实际上所有对象都可以被比较、检测逻辑值,以及转换为字符串（使用 repr() 函数或略有差异的 str() 函数).
# 后一个函数是在对象由 print() 函数输出时被隐式地调用的。

# NOTE 逻辑值检测

# 任何对象都可以进行逻辑值的检测，以便在 if 或 while 作为条件或是作为下文所述布尔运算的操作数来使用。

# 一个对象在默认情况下均被视为真值，除非当该对象被调用时其所属类定义了 __bool__() 方法且返回 False 或是定义了 __len__() 方法且返回零。

# 下面基本完整地列出了会被视为假值的内置对象:
# 1, 被定义为假值的常量: None 和 False。
# 2, 任何数值类型的零: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# 3, 空的序列和多项集: '', (), [], {}, set(), range(0)

# 产生布尔值结果的运算和内置函数总是返回 0 或 False 作为假值，1 或 True 作为真值，除非另行说明。
# （重要例外：布尔运算 or 和 and 总是返回其中一个操作数。）

# NOTE 布尔运算 --- and, or, not

# 这些属于布尔运算，按优先级升序排列:

# x or y
# if x is false, then y, else x
# 这是个短路运算符，因此只有在第一个参数为假值时才会对第二个参数求值。

# x and y
# if x is false, then x, else y
# 这是个短路运算符，因此只有在第一个参数为真值时才会对第二个参数求值。

# not x
# if x is false, then True, else False
# not 的优先级比非布尔运算符低，因此 not a == b 会被解读为 not (a == b) 而 a == not b 会引发语法错误。

# NOTE 比较

# 在 Python 中有八种比较运算符。 它们的优先级相同（比布尔运算的优先级高）。
# 比较运算可以任意串连；例如，x < y <= z 等价于 x < y and y <= z，前者的不同之处在于 y 只被求值一次
# （但在两种情况下当 x < y 结果为假值时 z 都不会被求值).

# 为什么会有严格两个字呢? (个人理解)
# 严格可能会检查类型匹配  例如 3 == '3', 3 < '5'
# (在js里面有 == 和 ===, js里面写 3 == '3'是符合的, 因为js这个==不检查类型, ===才检查类型
# <,>符号也是一样道理, 严格二字同样的道理

# 或者说  < 就是严格小于, <= 就是非严格小于 ?

# <           严格小于
# <=          小于或等于
# >           严格大于
# >=          大于或等于
# ==          等于
# !=          不等于
# is          对象标识
# is not      否定的对象标识

# 除了不同数字类型以外，不同类型的对象比较时绝对不会相等。
# 而且，某些类型（例如函数对象）仅支持简化比较形式，即任何两个该种类型的对象必定不相等。

# <, <=, > 和 >= 运算符在以下情况中将引发 TypeError 异常：

# 当比较复数与另一个内置数字类型时，当两个对象具有无法被比较的不同类型时，或在未定义次序的其他情况时。

# 具有不同标识的类的实例比较结果通常为不相等，除非类定义了 __eq__() 方法。

# 一个类实例不能与相同类或的其他实例或其他类型的对象进行排序，除非该类定义了足够多的方法，
# 包括 __lt__(), __le__(), __gt__() 以及 __ge__() (而如果你想实现常规意义上的比较操作，通常只要有 __lt__() 和 __eq__() 就可以了)。

# is 和 is not 运算符无法自定义；并且它们可以被应用于任意两个对象而不会引发异常。

# 还有两种具有相同语法优先级的运算 in 和 not in，它们被 iterable 或实现了 __contains__() 方法的类型所支持。

# NOTE 数字类型 --- int, float, complex

# 存在三种不同的数字类型: 整数, 浮点数 和 复数。 此外，布尔值属于整数的子类型。整数具有无限的精度。

# 浮点数通常使用 C 中的 double 来实现；有关你的程序运行所在机器上浮点数的精度和内部表示法可在 sys.float_info 中查看。

# import sys
# print(sys.float_info)

# 复数包含实部和虚部，分别以一个浮点数表示。
# 要从一个复数z中提取这两个部分，可使用z.real和z.imag。
# (标准库包含附加的数字类型，如表示有理数的fractions以及以用户定制精度表示浮点数的decimal.)

# 数字是由数字字面值或内置函数与运算符的结果来创建的。
# 不带修饰的整数字面值（包括十六进制、八进制和二进制数）会生成整数。

# 包含小数点或幂运算符的数字字面值会生成浮点数。

# 在数字字面值末尾加上 'j' 或 'J' 会生成虚数（实部为零的复数），你可以将其与整数或浮点数相加来得到具有实部和虚部的复数。

# Python 完全支持混合算术：
# 当一个二元运算符用于不同数字类型的操作数时，具有“较窄” 类型的操作数会被扩展为另操作数的类型，整数比浮点数更窄，浮点数又比复数更窄。

# 混合类型数字之间的比较也使用相同的规则。因此，列表[1,2]被认为等于[1.0,2.0]，并且类似于元组。

# 构造器 int(), float() 和 complex() 可被用于生成特定类型的数字。

# 所有数字类型（复数除外）都支持下列运算，按优先级升序排序（所有数字运算的优先级都高于比较运算）

# 运算

# x + y                     x 和 y 的和
# x - y                     x 和 y 的差
# x * y                     x 和 y 的乘积
# x / y                     x 和 y 的商

# x // y                    x 和 y 的商数
# 也称为整数除法。 结果值是一个整数，但结果的类型不一定是 int。
# 运算结果总是向负无穷的方向舍入: 1//2 为 0, (-1)//2 为 -1, 1//(-2) 为 -1 而 (-1)//(-2) 为 0。

# x % y                     (x / y)的余数
# 不可用于复数。 而应在适当条件下使用 abs() 转换为浮点数。

# -x                        x 取反
# +x                        x 不变
# abs(x)                    x 的绝对值或大小

# int(x)                    将 x 转换为整数
# 从浮点数转换为整数会被舍入或是像在 C 语言中一样被截断；请参阅 math.floor() 和 math.ceil() 函数查看转换的完整定义。
# 接受的数字字面值包括数码 0 到 9 或任何等效的 Unicode 字符（具有 Nd 特征属性的代码点）。
# 请参阅 http://www.unicode.org/Public/10.0.0/ucd/extracted/DerivedNumericType.txt 查看具有 Nd 特征属性的代码点的完整列表。

# float(x)                  将 x 转换为浮点数
# float 也接受字符串 "nan" 和附带可选前缀 "+" 或 "-" 的 "inf" 分别表示非数字 (NaN) 以及正或负无穷。
# 接受的数字字面值包括数码 0 到 9 或任何等效的 Unicode 字符（具有 Nd 特征属性的代码点）。
# 请参阅 http://www.unicode.org/Public/10.0.0/ucd/extracted/DerivedNumericType.txt 查看具有 Nd 特征属性的代码点的完整列表。

# complex(re, im)           一个带有实部 re 和虚部 im 的复数。im 默认为0。
# 接受的数字字面值包括数码 0 到 9 或任何等效的 Unicode 字符（具有 Nd 特征属性的代码点）。
# 请参阅 http://www.unicode.org/Public/10.0.0/ucd/extracted/DerivedNumericType.txt 查看具有 Nd 特征属性的代码点的完整列表。

# c.conjugate()             复数 c 的共轭

# divmod(x, y)              (x // y, x % y)
# 不可用于复数。 而应在适当条件下使用 abs() 转换为浮点数。

# pow(x, y)                 x 的 y 次幂
# x ** y                    x 的 y 次幂

# Python 将 pow(0, 0) 和 0 ** 0 定义为 1，这是编程语言的普遍做法。

# 所有 numbers.Real 类型 (int 和 float) 还包括下列运算:

# 运算
# math.trunc(x)         x 截断为 Integral
# round(x[, n])         x 舍入到 n 位小数，半数值会舍入到偶数。 如果省略 n，则默认为 0。
# math.floor(x)         <= x 的最大 Integral
# math.ceil(x)          >= x 的最小 Integral

# 有关更多的数字运算请参阅 math 和 cmath 模块。

# NOTE 整数类型的按位运算

# 按位运算只对整数有意义。

# 计算按位运算的结果，就相当于使用无穷多个二进制符号位对二的补码执行操作。

# 二进制按位运算的优先级全都低于数字运算，但又高于比较运算；一元运算 ~ 具有与其他一元算术运算 (+ and -) 相同的优先级。

# 此表格是以优先级升序排序的按位运算列表:

# x | y	        x 和 y 按位 或      (4)
# x ^ y         x 和 y 按位 异或     (4)
# x & y         x 和 y 按位 与      (4)
# x << n	    x 左移 n 位         (1)(2)
# x >> n	    x 右移 n 位         (1)(3)
# ~x            x 逐位取反

# 注释:
#
# 1, 负的移位数是非法的，会导致引发 ValueError。
# 2, 左移 n 位等价于不带溢出检测地乘以 pow(2, n)。
# 3, 右移 n 位等价于不带溢出检测地除以 pow(2, n)。
# 4, 使用带有至少一个额外符号扩展位的有限个二进制补码表示（有效位宽度为 1 + max(x.bit_length(), y.bit_length()) 或以上）
# 执行这些计算就足以获得相当于有无数个符号位时的同样结果。

# NOTE 整数类型的附加方法

# int 类型实现了 numbers.Integral abstract base class。 此外，它还提供了其他几个方法:

# 1, int.bit_length()
# 返回以二进制表示一个整数所需要的位数，不包括符号位和前面的零:

n = -37
l_log(bin(n))
l_log(n.bit_length())


# 更准确地说，如果 x 非零，则 x.bit_length() 是使得 2**(k-1) <= abs(x) < 2**k 的唯一正整数 k。
# 同样地，当 abs(x) 小到足以具有正确的舍入对数时，则 k = 1 + int(log(abs(x), 2))。 如果 x 为零，则 x.bit_length() 返回 0。

# 等价于:

def bit_length(self):
    s = bin(self)  # binary representation:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b')  # remove leading zeros and minus sign
    return len(s)  # len('100101') --> 6


# 3.1 新版功能.
# 2, int.to_bytes(length, byteorder, *, signed=False)
# 返回表示一个整数的字节数组。

l_log((1024).to_bytes(2, byteorder='big'))
l_log((1024).to_bytes(10, byteorder='big'))
l_log((-1024).to_bytes(10, byteorder='big', signed=True))
x = 1000
l_log(x.to_bytes((x.bit_length() + 7) // 8, byteorder='little'))

# 整数会使用 length 个字节来表示。 如果整数不能用给定的字节数来表示则会引发 OverflowError。

# byteorder 参数确定用于表示整数的字节顺序。
# 如果 byteorder 为 "big"，则最高位字节放在字节数组的开头。
# 如果 byteorder 为 "little"，则最高位字节放在字节数组的末尾。
# 要请求主机系统上的原生字节顺序，请使用 sys.byteorder 作为字节顺序值。

# signed 参数确定是否使用二的补码来表示整数。
# 如果 signed 为 False 并且给出的是负整数，则会引发 OverflowError。
# signed 的默认值为 False。

# NOTE 3.2 新版功能.

# class method int.from_bytes(bytes, byteorder, *, signed=False)
# 返回由给定字节数组所表示的整数。

l_log(int.from_bytes(b'\x00\x10', byteorder='big'))

l_log(int.from_bytes(b'\x00\x10', byteorder='little'))

l_log(int.from_bytes(b'\xfc\x00', byteorder='big', signed=True))

l_log(int.from_bytes(b'\xfc\x00', byteorder='big', signed=False))

l_log(int.from_bytes([255, 0, 0], byteorder='big'))

# bytes 参数必须为一个 bytes-like object 或是生成字节的可迭代对象。

# byteorder 参数确定用于表示整数的字节顺序。
# 如果 byteorder 为 "big"，则最高位字节放在字节数组的开头。
# 如果 byteorder 为 "little"，则最高位字节放在字节数组的末尾。
# 要请求主机系统上的原生字节顺序，请使用 sys.byteorder 作为字节顺序值。

# signed 参数指明是否使用二的补码来表示整数。

# NOTE 3.2 新版功能.

# NOTE 浮点类型的附加方法

# float 类型实现了 numbers.Real abstract base class。 float 还具有以下附加方法。

# 1, float.as_integer_ratio()
# 返回一对整数，其比率正好等于原浮点数并且分母为正数。 无穷大会引发 OverflowError 而 NaN 则会引发 ValueError。

# 2, float.is_integer()
# 如果 float 实例可用有限位整数表示则返回 True，否则返回 False:

l_log((-2.0).is_integer())
l_log((3.2).is_integer())

# 两个方法均支持与十六进制数字符串之间的转换。
# 由于 Python 浮点数在内部存储为二进制数，因此浮点数与 十进制数 字符串之间的转换往往会导致微小的舍入错误。
# 而十六进制数字符串却允许精确地表示和描述浮点数。
# 这在进行调试和数值工作时非常有用。

# 3, float.hex()
# 以十六进制字符串的形式返回一个浮点数表示。 对于有限浮点数，这种表示法将总是包含前导的 0x 和尾随的 p 加指数。

l_log(2.1.hex())

# 4, class method float.fromhex(s)
# 返回以十六进制字符串 s 表示的浮点数的类方法。 字符串 s 可以带有前导和尾随的空格。

# 请注意 float.hex() 是实例方法，而 float.fromhex() 是类方法。

# 十六进制字符串采用的形式为:
# [sign] ['0x'] integer ['.' fraction] ['p' exponent]

# 可选的 sign 可以是 + 或 -，integer 和 fraction 是十六进制数码组成的字符串，exponent 是带有可选前导符的十进制整数。
# 大小写没有影响，在 integer 或 fraction 中必须至少有一个十六进制数码。
# 此语法类似于 C99 标准的 6.4.4.2 小节中所描述的语法，也是 Java 1.5 以上所使用的语法。
# 特别地，float.hex() 的输出可以用作 C 或 Java 代码中的十六进制浮点数字面值，
# 而由 C 的 %a 格式字符或 Java 的 Double.toHexString 所生成的十六进制数字符串由为 float.fromhex() 所接受。

# 请注意 exponent 是十进制数而非十六进制数，它给出要与系数相乘的 2 的幂次。
# 例如，十六进制数字符串 0x3.a7p10 表示浮点数 (3 + 10./16 + 7./16**2) * 2.0**10 即 3740.0:

l_log(float.fromhex('0x3.a7p10'))

# 对 3740.0 应用反向转换会得到另一个代表相同数值的十六进制数字符串:

l_log(float.hex(3740.0))

# NOTE 数字类型的哈希运算

# 对于可能为不同类型的数字 x 和 y，要求 x == y 时必定 hash(x) == hash(y) (详情参见 __hash__() 方法的文档)。

# 为了便于在各种数字类型 (包括 int, float, decimal.Decimal 和 fractions.Fraction) 上实现并保证效率，
# Python 对数字类型的哈希运算是基于为任意有理数定义统一的数学函数，因此该运算对 int 和 fractions.Fraction 的全部实例，
# 以及 float 和 decimal.Decimal 的全部有限实例均可用.

# 从本质上说，此函数是通过以一个固定质数 P 进行 P 降模给出的。
# P 的值在 Python 中可以 sys.hash_info 的 modulus 属性的形式被访问。

# CPython implementation detail: 目前所用的质数设定，
# 在 C long 为 32 位的机器上 P = 2**31 - 1 而在 C long 为 64 位的机器上 P = 2**61 - 1。

# 详细规则如下所述:

# 1, 如果 x = m / n 是一个非负的有理数且 n 不可被 P 整除，则定义 hash(x) 为 m * invmod(n, P) % P，
# 其中 invmod(n, P) 是对 n 模 P 取反。

# 2, 如果 x = m / n 是一个非负的有理数且 n 可被 P 整除（但 m 不能）则 n 不能对 P 降模，
# 以上规则不适用；在此情况下则定义 hash(x) 为常数值 sys.hash_info.inf。

# 3, 如果 x = m / n 是一个负的有理数则定义 hash(x) 为 -hash(-x)。 如果结果哈希值为 -1 则将其替换为 -2。

# 4, 特定值 sys.hash_info.inf, -sys.hash_info.inf 和 sys.hash_info.nan 被用作正无穷、负无穷和空值（所分别对应的）哈希值。
# （所有可哈希的空值都具有相同的哈希值。）

# 5, 对于一个 complex 值 z，会通过计算 hash(z.real) + sys.hash_info.imag * hash(z.imag) 将实部和虚部的哈希值结合起来，
# 并进行降模 2**sys.hash_info.width 以使其处于 range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width - 1)) 范围之内。
#  同样地，如果结果为 -1 则将其替换为 -2。

# 为了阐明上述规则，这里有一些等价于内置哈希算法的 Python 代码示例，可用于计算有理数、float 或 complex 的哈希值:

import sys, math


def hash_fraction(m, n):
    """计算有理数m / n的散列.

    假设m和n是整数，n为正。
    相当于hash（fractions.Fraction（m，n））.

    """
    P = sys.hash_info.modulus
    # 去除P.的常见因素（如果m和n已经是互质的，则不必要。）
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem:
        # pow（n，P-1，P）为1，因此pow（n，P-2，P）给出n模P的倒数。
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value


def hash_float(x):
    """计算浮点x的哈希值。"""

    if math.isnan(x):
        return sys.hash_info.nan
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())


def hash_complex(z):
    """计算复数z的哈希值。"""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2 ** (sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value


# NOTE 迭代器类型

# Python 支持在容器中进行迭代的概念。
# 这是通过使用两个单独方法来实现的；它们被用于允许用户自定义类对迭代的支持。
# 将在下文中详细描述的序列总是支持迭代方法。

# 容器对象要提供迭代支持，必须定义一个方法:

# container.__iter__()

# 返回一个迭代器对象。 该对象需要支持下文所述的迭代器协议。
# 如果容器支持不同的迭代类型，则可以提供额外的方法来专门地请求不同迭代类型的迭代器。
# （支持多种迭代形式的对象的例子有同时支持广度优先和深度优先遍历的树结构。）
# 此方法对应于 Python/C API 中 Python 对象类型结构体的 tp_iter 槽位。

# 迭代器对象自身需要支持以下两个方法，它们共同组成了 迭代器协议:

# iterator.__iter__()
# 返回迭代器对象本身。 这是同时允许容器和迭代器配合 for 和 in 语句使用所必须的。
# 此方法对应于 Python/C API 中 Python 对象类型结构体的 tp_iter 槽位。

# iterator.__next__()
# 从容器中返回下一项。 如果已经没有项可返回，则会引发 StopIteration 异常。
# 此方法对应于 Python/C API 中 Python 对象类型结构体的 tp_iternext 槽位。

# Python 定义了几种迭代器对象以支持对一般和特定序列类型、字典和其他更特别的形式进行迭代。
# 除了迭代器协议的实现，特定类型的其他性质对迭代操作来说都不重要。

# 一旦迭代器的 __next__() 方法引发了 StopIteration，它必须一直对后续调用引发同样的异常。
# 不遵循此行为特性的实现将无法正常使用。

# NOTE 生成器类型

# Python 的 generator 提供了一种实现迭代器协议的便捷方式。
# 如果容器对象 __iter__() 方法被实现为一个生成器，它将自动返回一个迭代器对象（从技术上说是一个生成器对象），
# 该对象提供 __iter__() 和 __next__() 方法。 有关生成器的更多信息可以参阅 yield 表达式的文档。

# NOTE 序列类型 --- list, tuple, range

# 有三种基本序列类型：list, tuple 和 range 对象。 为处理 二进制数据 和 文本字符串 而特别定制的附加序列类型会在专门的小节中描述。

# NOTE 通用序列操作

# 大多数序列类型，包括可变类型和不可变类型都支持下表中的操作。
# collections.abc.Sequence ABC 被提供用来更容易地在自定义序列类型上正确地实现这些操作。

# 此表按优先级升序列出了序列操作。
# 在表格中，s 和 t 是具有相同类型的序列，n, i, j 和 k 是整数而 x 是任何满足 s 所规定的类型和值限制的任意对象。

# in 和 not in 操作具有与比较操作相同的优先级。
# + (拼接) 和 * (重复) 操作具有与对应数值运算相同的优先级。


# x in s
# 如果 s 中的某项等于 x 则结果为 True，否则为 False (注释:1)

# x not in s
# 如果 s 中的某项等于 x 则结果为 False，否则为 True (注释:1)

# s + t
# s 与 t 相拼接 (注释:6,7)

# s * n 或 n * s
# 相当于 s 与自身进行 n 次拼接 (注释:2,7)

# s[i]
# s 的第 i 项，起始为 0 (注释3)

# s[i:j]
# s 从 i 到 j 的切片 (注释3,4)

# s[i:j:k]
# s 从 i 到 j 步长为 k 的切片 (注释3,5)

# len(s)
# s的长度

# min(s)
# s 的最小项

# max(s)
# s 的最大项

# s.index(x[, i[, j]])
# x 在 s 中首次出现项的索引号（索引号在 i 或其后且在 j 之前）(注释8)

# s.count(x)
# x 在 s 中出现的总次数

# 相同类型的序列也支持比较。 特别地，tuple 和 list 的比较是通过比较对应元素的字典顺序。
# 这意味着想要比较结果相等，则每个元素比较结果都必须相等，并且两个序列长度必须相同。
# （完整细节请参阅语言参考的 比较运算 部分。）

# 注释:
# 1, 虽然 in 和 not in 操作在通常情况下仅被用于简单的成员检测，某些专门化序列
# (例如 str, bytes 和 bytearray) 也使用它们进行子序列检测:
l_log("gg" in "eggs")

# 2, 小于 0 的 n 值会被当作 0 来处理 (生成一个与 s 同类型的空序列)。
# 请注意序列 s 中的项并不会被拷贝；它们会被多次引用。 这一点经常会令 Python 编程新手感到困扰；例如:
lists = [[]] * 3
l_log(lists)
lists[0].append(3)
l_log(lists)

# 具体的原因在于 [[]] 是一个包含了一个空列表的单元素列表，所以 [[]] * 3 结果中的三个元素都是对这一个空列表的引用。
# 修改 lists 中的任何一个元素实际上都是对这一个空列表的修改。 你可以用以下方式创建以不同列表为元素的列表:

lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
l_log(lists)

# 3, 如果 i 或 j 为负值，则索引顺序是相对于序列 s 的末尾: 索引号会被替换为 len(s) + i 或 len(s) + j。
# 但要注意 -0 仍然为 0。

# 4, s 从 i 到 j 的切片被定义为所有满足 i <= k < j 的索引号 k 的项组成的序列。
# 如果 i 或 j 大于 len(s)，则使用 len(s)。 如果 i 被省略或为 None，则使用 0。
# 如果 j 被省略或为 None，则使用 len(s)。 如果 i 大于等于 j，则切片为空。

# 5, s 从 i 到 j 步长为 k 的切片被定义为所有满足 0 <= n < (j-i)/k 的索引号 x = i + n*k 的项组成的序列。
# 换句话说，索引号为 i, i+k, i+2*k, i+3*k，以此类推，当达到 j 时停止 (但一定不包括 j)。
# 当 k 为正值时，i 和 j 会被减至不大于 len(s)。
# 当 k 为负值时，i 和 j 会被减至不大于 len(s) - 1。
# 如果 i 或 j 被省略或为 None，它们会成为“终止”值 (是哪一端的终止值则取决于 k 的符号)。
# 请注意，k 不可为零。 如果 k 为 None，则当作 1 处理。

# 6, 拼接不可变序列总是会生成新的对象。 这意味着通过重复拼接来构建序列的运行时开销将会基于序列总长度的乘方。
# 想要获得线性的运行时开销，你必须改用下列替代方案之一：

# 如果拼接 str 对象，你可以构建一个列表并在最后使用 str.join() 或是写入一个 io.StringIO 实例并在结束时获取它的值

# 如果拼接 bytes 对象，你可以类似地使用 bytes.join() 或 io.BytesIO，或者你也可以使用 bytearray 对象进行原地拼接。
# bytearray 对象是可变的，并且具有高效的重分配机制

# 如果拼接 tuple 对象，请改为扩展 list 类

# 对于其它类型，请查看相应的文档

# 7, 某些序列类型 (例如 range) 仅支持遵循特定模式的项序列，因此并不支持序列拼接或重复。

# 8, 当 x 在 s 中找不到时 index 会引发 ValueError。 不是所有实现都支持传入额外参数 i 和 j。
# 这两个参数允许高效地搜索序列的子序列。
# 传入这两个额外参数大致相当于使用 s[i:j].index(x)，但是不会复制任何数据，并且返回的索引是相对于序列的开头而非切片的开头。

# NOTE 不可变序列类型

# 不可变序列类型普遍实现而可变序列类型未实现的唯一操作就是对 hash() 内置函数的支持。
# 这种支持允许不可变类型，例如 tuple 实例被用作 dict 键，以及存储在 set 和 frozenset 实例中。
# 尝试对包含有不可哈希值的不可变序列进行哈希运算将会导致 TypeError。

# NOTE 可变序列类型

# 以下表格中的操作是在可变序列类型上定义的。
# collections.abc.MutableSequence ABC 被提供用来更容易地在自定义序列类型上正确实现这些操作。
# 表格中的 s 是可变序列类型的实例，t 是任意可迭代对象，而 x 是符合对 s 所规定类型与值限制的任何对象
# (例如，bytearray 仅接受满足 0 <= x <= 255 值限制的整数)。

# 运算

# s[i] = x
# 将 s 的第 i 项替换为 x

# s[i:j] = t
# 将 s 从 i 到 j 的切片替换为可迭代对象 t 的内容

# del s[i:j]
# 等同于 s[i:j] = []

# s[i:j:k] = t  (注释: 1)
# 将 s[i:j:k] 的元素替换为 t 的元素

# del s[i:j:k]
# 从列表中移除 s[i:j:k] 的元素

# s.append(x)
# 将 x 添加到序列的末尾 (等同于 s[len(s):len(s)] = [x])

# s.clear() (注释: 5)
# 从 s 中移除所有项 (等同于 del s[:])

# s.copy()  (注释: 5)
# 创建 s 的浅拷贝 (等同于 s[:])

# s.extend(t) 或 s += t
# 用 t 的内容扩展 s (基本上等同于 s[len(s):len(s)] = t)

# s *= n (注释: 6)
# 使用 s 的内容重复 n 次来对其进行更新

# s.insert(i, x)
# 在由 i 给出的索引位置将 x 插入 s (等同于 s[i:i] = [x])

# s.pop([i]) (注释: 2)
# 提取在 i 位置上的项，并将其从 s 中移除

# s.remove(x) (注释: 3)
# 删除 s 中第一个 s[i] 等于 x 的项目。

# s.reverse() (注释: 4)
# 就地将列表中的元素逆序。

# 注释:
# 1, t 必须与它所替换的切片具有相同的长度。

# 2. 可选参数 i 默认为 -1，因此在默认情况下会移除并返回最后一项。

# 3. 当在 s 中找不到 x 时 remove 操作会引发 ValueError。

# 4. 当反转大尺寸序列时 reverse() 方法会原地修改该序列以保证空间经济性。 为提醒用户此操作是通过间接影响进行的，它并不会返回反转后的序列。

# 5. 包括 clear() 和 copy() 是为了与不支持切片操作的可变容器 (例如 dict 和 set) 的接口保持一致
#    3.3 新版功能: clear() 和 copy() 方法。

# 6. n 值为一个整数，或是一个实现了 __index__() 的对象。 n 值为零或负数将清空序列。
# 序列中的项不会被拷贝；它们会被多次引用，正如 通用序列操作 中有关 s * n 的说明。

# NOTE 列表

# 列表是可变序列，通常用于存放同类项目的集合（其中精确的相似程度将根据应用而变化）。

# class list([iterable])
#   可以用多种方式构建列表：

# 使用一对方括号来表示空列表: []
# 使用方括号，其中的项以逗号分隔: [a], [a, b, c]
# 使用列表推导式: [x for x in iterable]
# 使用类型的构造器: list() 或 list(iterable)

# 构造器将构造一个列表，其中的项与 iterable 中的项具有相同的的值与顺序。
# iterable 可以是序列、支持迭代的容器或其它可迭代对象。
# 如果 iterable 已经是一个列表，将创建并返回其副本，类似于 iterable[:]。
# 例如，list('abc') 返回 ['a', 'b', 'c'] 而 list( (1, 2, 3) ) 返回 [1, 2, 3]。
# 如果没有给出参数，构造器将创建一个空列表 []。

# 其它许多操作也会产生列表，包括 sorted() 内置函数。

# 列表实现了所有 一般 和 可变 序列的操作。 列表还额外提供了以下方法：
