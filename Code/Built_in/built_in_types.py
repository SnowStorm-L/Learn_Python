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
    s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b') # remove leading zeros and minus sign
    return len(s)       # len('100101') --> 6


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

# 3.2 新版功能.

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

