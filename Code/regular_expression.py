#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 PM2:00
# @Author  : L
# @Email   : L862608263@163.com
# @File    : regular_expression.py
# @Software: PyCharm


# 正则表达式介绍
#
# 正则表达式（Regular expressions 也称为 REs，或 regexes 或 regex patterns）本质上是一个微小的且高度专业化的编程语言。
# 它被嵌入到 Python 中，并通过 re 模块提供给程序猿使用。
# 使用正则表达式，你需要指定一些规则来描述那些你希望匹配的字符串集合。
# 这些字符串集合可能包含英语句子、 e-mail 地址、TeX 命令，或任何你想要的东东。
#
# 正则表达式模式被编译成一系列的字节码，然后由一个 C 语言写的匹配引擎所执行。
# 对于高级的使用，你可能需要更关注匹配引擎是如何执行给定的 RE，并通过一定的方式来编写 RE，以便产生一个可以运行得更快的字节码。


import re

# print(re.__doc__)

# NOTE re模块 特殊字符

# 字符            描述
# .             匹配除换行符之外的任何字符。
# ^             匹配字符串的开头。
# $             匹配字符串的结尾 或 紧挨在字符串末尾的换行符 之前的
# *             匹配前一个字符,0次或无限次(贪婪匹配)  例: 匹配条件adc*, 结果ad或adcccc
# +             匹配前一个字符,1次或无限次(贪婪匹配)  例: 匹配条件adc+, 结果adc或adcccc
# ?             匹配前一个字符,0次或1次(贪婪匹配)    例: 匹配条件adc?, 结果ad或adc
# *? +? ??      前三个特殊字符的非贪婪版本。
# {m,n}         匹配前一个字符m到n次,m或n可以省略.
#               若省略m, {,n} 则匹配0至n次
#               若省略n, {m} 匹配m次
# {m,n}?        {m,n}的非贪婪版本。
# \\            转义特殊字符 或 signals a special sequence.(没看懂这句什么意思, 可能是后面\\\一堆的意思) 正则表达式匹配反斜杠"\","\\\\" 或 r"\\"
# []            表示一组字符。作为第一个字符的“^”表示补充集合。


# NOTE re模块 修饰符 - 可选标志 介绍
# re模块提供的方法基本都带有flags参数, flags参数是个默认参数 flags = 0
# flags标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
# 修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志

# 修饰符                 描述
# re.A    ASCII         对于字符串模式，使\ w，\ W，\ b，\ B，\ d，\ D匹配相应的ASCII字符类别（而不是整个Unicode类别，默认）。
#                       对于字节模式，此标志是唯一可用的行为，不需要指定。
# re.L    LOCALE        影响 \w, \W, \b, \B 依赖于当前的语言环境。
# re.I    IGNORECASE    执行不区分大小写的匹配。
# re.M    MULTILINE     “^”匹配行的开头（换行符后）以及字符串。“$”匹配行的末尾（换行符之前）以及字符串的结尾。
# re.S    DOTALL        “.” 完全匹配任何字符，包括换行符。
# re.X    VERBOSE       忽略空符，并可以加入注释,如下a和b是等价的
#                       a = re.compile(r"""\d +  # the integral part
#                                          \.    # the decimal point
#                                          \d *  # some fractional digits""", re.X)
#                       b = re.compile(r"\d+\.\d*")
# re.U    UNICODE       仅用于兼容性。 忽略字符串模式（这是默认值），禁止字节模式。

# NOTE re模块 提供的方法介绍

# 1, re.match(pattern, string, flags=0)
# 将正则表达式模式匹配到字符串的开头。(验证字符串开头, 是否符合匹配规则)
# pattern      匹配的正则表达式
# string       要匹配的字符串。


# match完之后
# 使用group(num) 或 groups() 来获取匹配结果
# 使用span()获取匹配结果的范围 返回元组, 其实就是start(), end() 2个返回的范围

# Demo
# matchObj = re.match('www', 'www.run_oob.com')
# print(matchObj.group())
# print(matchObj.span())
#
# matchObj = re.match(r'(.*) are (.*?) .*', "Cats are smarter than dogs", re.M | re.I)
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

# 2, re.fullmatch(pattern, string, flags=0)
# 将正则表达式模式匹配到所有字符串。  (找整个字符串, 验证是否符合匹配规则)

# Demo
# matchObj = re.fullmatch('www.bai.com', 'www.bai.com')
# print(matchObj)


# 下边是元字符的完整列表（我们将在后边逐一讲解）：
#
# .   ^   $   *   +   ?   { }   [ ]   \   |   ( )

# []

# 我们先来看下方括号 [ ]，它们指定一个字符类用于存放你需要匹配的字符集合。
# 可以单独列出需要匹配的字符，也可以通过两个字符和一个横杆 - 指定匹配的范围。
# 例如
# [abc] 会匹配字符 a，b 或 c；
# [a-c] 可以实现相同的功能。
# 后者使用范围来表示与前者相同的字符集合。
# 如果你想只匹配小写字母，你的 RE 可以写成 [a-z]
