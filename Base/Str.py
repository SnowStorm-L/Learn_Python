# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 PM3:12
# @Author  : L
# @Email   : L862608263@163.com
# @File    : Str.py
# @Software: PyCharm

newStr = 'python python'

print(newStr[:7])

print(newStr[1])

# 不能被修改
# TypeError: 'str' object does not support item assignment
# newStr[0] = 'd'

newStr = 'jjJJjj' + newStr[6:]

print(newStr)

# format方法
# 位置参数
"{0} love {1}.{2}".format("i", "google", "com")

# 关键字参数
"{a} love {b}.{c}".format(a="i", b="google", c="com")

# 两种可以混合使用,但位置参数必须在关键字参数之前

# 错误示范
# SyntaxError: positional argument follows keyword argument
# "{a}.{b}.{0}".format(a='1', b='2', '3')

# 没打印括号2个字
print("{{0}}".format("括号"))

# 在替换域中 冒号表示格式化的开始  .1f 保留一位小数(四舍五入)
print("{0:.1f}{1}".format(27.55, 'GB'))

# 字符串格式化符号含义
#
# 符号              说明
# %c      格式化字符及其 ASCII 码
# %s      格式化字符串%d 格式化整数
# %o      格式化无符号八进制数
# %x      格式化无符号十六进制数
# %X      格式化无符号十六进制数（大写）
# %f      格式化浮点数字，可指定小数点后的精度
# %e      用科学计数法格式化浮点数
# %E      作用同 %e，用科学计数法格式化浮点数
# %g      根据值的大小决定使用 %f 或 %e
# %G      作用同 %g，根据值的大小决定使用 %f 或者 %E
#
#
# 格式化操作符辅助命令
#
# 符号             说明
# m.n m    是显示的最小总宽度，n 是小数点后的位数
# -        用于左对齐
# +        在正数前面显示加号（+）
# #        在八进制数前面显示 '0o'，在十六进制数前面显示 '0x' 或 '0X'
# 0        显示的数字前面填充 '0' 取代空格
#
#
# Python 的转义字符及其含义
#
# 符号              说明
# \'              单引号
# \"              双引号
# \a              发出系统响铃声
# \b              退格符
# \n              换行符
# \t              横向制表符（TAB）
# \v              纵向制表符
# \r              回车符
# \f              换页符
# \o              八进制数代表的字符
# \x              十六进制数代表的字符
# \0              表示一个空字符
# \\              反斜杠

# 字符串的各种方法

# capitalize()
# 把字符串的第一个字符改为大写

print(newStr.capitalize())

# casefold()
# 把整个字符串的所有字符改为小写

print(newStr.casefold())

# center(width)
# 将字符串居中，并使用空格填充至长度width的新字符串

print(newStr.center(40, 'a'))

# count(sub[, start[, end]])
# 返回sub在字符串里边出现的次数，start和end参数表示范围，可选。

# encode(encoding='utf-8', errors='strict')
# 以encoding指定的编码格式对字符串进行编码。

# endswith(sub[, start[, end]])
# 检查字符串是否以sub子字符串结束，如果是返回True，否则返回False。start和end参数表示范围，可选。

# expandtabs([tabsize = 8])
# 把字符串中的tab符号（\t）转换为空格，如不指定参数，默认的空格数是tabsize = 8。

# find(sub[, start[, end]])
# 检测sub是否包含在字符串中，如果有则返回索引值，否则返回 - 1，start和end参数表示范围，可选。

# index(sub[, start[, end]])
# 跟find方法一样，不过如果sub不在string中会产生一个异常。

# isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False。

# isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False。

# isdecimal()
# 如果字符串只包含十进制数字则返回True，否则返回False。

# isdigit()
# 如果字符串只包含数字则返回True，否则返回False。

# islower()
# 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回True，否则返回False。

# isnumeric()
# 如果字符串中只包含数字字符，则返回True，否则返回False。

# isspace()
# 如果字符串中只包含空格，则返回True，否则返回False。

# istitle()
# 如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回True，否则返回False。

# isupper()
# 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回True，否则返回False。

# join(sub)
# 以字符串作为分隔符，插入到sub中所有的字符之间。

# ljust(width)
# 返回一个左对齐的字符串，并使用空格填充至长度为width的新字符串。

# lower()
# 转换字符串中所有大写字符为小写。

# lstrip()
# 去掉字符串左边的所有空格

# partition(sub)
# 找到子字符串sub，把字符串分成一个3元组(pre_sub, sub, fol_sub)，如果字符串中不包含sub则返回('原字符串', '', '')

# replace(old, new[, count])
# 把字符串中的old子字符串替换成new子字符串，如果count指定，则替换不超过count次。

# rfind(sub[, start[, end]])
# 类似于find()方法，不过是从右边开始查找。

# rindex(sub[, start[, end]])
# 类似于index()方法，不过是从右边开始。

# rjust(width)
# 返回一个右对齐的字符串，并使用空格填充至长度为width的新字符串。

# rpartition(sub)
# 类似于partition()方法，不过是从右边开始查找。

# rstrip()
# 删除字符串末尾的空格。

# split(sep=None, maxsplit=-1)
# 不带参数默认是以空格为分隔符切片字符串，如果maxsplit参数有设置，则仅分隔maxsplit个子字符串，返回切片后的子字符串拼接的列表。

# splitlines(([keepends]))
# 按照'\n'分隔，返回一个包含各行作为元素的列表，如果keepends参数指定，则返回前keepends行。

# startswith(prefix[, start[, end]])
# 检查字符串是否以prefix开头，是则返回True，否则返回False。start和end参数可以指定范围检查，可选。

# strip([chars])
# 删除字符串前边和后边所有的空格，chars参数可以定制删除的字符，可选。

# swapcase()
# 翻转字符串中的大小写。

# title()
# 返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串。

# translate(table)
# 根据table的规则（可以由str.maketrans('a', 'b')定制）转换字符串中的字符。

# upper()
# 转换字符串中的所有小写字符为大写。

# zfill(width)
# 返回长度为width的字符串，原字符串右对齐，前边用0填充。

