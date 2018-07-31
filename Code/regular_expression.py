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
# |             A | B，创建一个与A或B匹配的RE。
# (...)         匹配括号内的RE。可以在字符串中稍后检索或匹配内容。
# (？aiLmsux)   设置RE的A，I，L，M，S，U或X标志（见下文）。
# (？：...)     常规括号的非分组版本。
# (?P<name>...) 组匹配的子字符串可通过名称访问。
# (?P=name)    匹配之前由名为name的组匹配的文本。
# (?#...)       A comment; ignored.
# (?=...)      匹配if ...匹配next，但不消耗字符串。
# (?!...)      匹配如果......下一个不匹配。
# (?<=...)     匹配如果前面有...（必须是固定长度）。
# (?<!...)     如果没有匹配，则匹配...（必须是固定长度）。
# (?(id/name)yes|no) 如果id / name匹配的组匹配yes模式，否则不使用匹配模式。

# NOTE re模块 特殊序列

# 特殊序列由“\\”和下面列表中的字符组成。
# 如果普通字符不在列表中，则生成的RE将匹配第二个字符。

# \number  匹配相同number的组的内容。 Matches the contents of the group of the same number.

# \A       只匹配字符串的开头。

# \Z       只匹配字符串的末尾。

# \b       匹配空字符串，但仅限于单词的开头或结尾。

# \B       匹配空字符串，但不匹配单词的开头或结尾。

# \d       匹配任何十进制数字; 相当于以字节模式设置的[0-9]或带有ASCII标志的字符串模式。
#          在没有ASCII标志的字符串模式中，它将匹配整个Unicode数字范围。

# \D       匹配任何非数字字符; 相当于[^ \ d]。

# \s       匹配任何空白字符; 等效于[\ t \ n \ r \ n \ f \ v]字节模式或带有ASCII标志的字符串模式。
#          在没有ASCII标志的字符串模式中，它将匹配整个Unicode空白字符范围。

# \S       匹配任何非空白字符; 相当于[^ \ s]。

# \w       匹配任何字母数字字符; 等效于字节模式中的[a-zA-Z0-9_]或带有ASCII标志的字符串模式。
#
#          在没有ASCII标志的字符串模式中，它将匹配Unicode字母数字字符的范围（字母加数字加下划线）。
#
#          使用LOCALE，它将匹配set [0-9_]加上定义为当前语言环境的字母的字符。

# \W       用于匹配所有与\w不匹配的字符
# \\       匹配反斜杠.


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

# NOTE 1, re.match(pattern, string, flags=0)
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

# NOTE 2, re.fullmatch(pattern, string, flags=0)
# 将正则表达式模式匹配到所有字符串。  (找整个字符串, 验证是否符合匹配规则)

# Demo
# matchObj = re.fullmatch('www.bai.com', 'www.bai.com')
# print(matchObj)

# NOTE 3, re.search(pattern, string, flags=0)
# 扫描整个字符串以查找与模式匹配的内容，返回第一个匹配对象，如果未找到匹配则返回None。

# Demo
# print(re.search("super", "man_super_sun_super"))

# NOTE search 和 match的区别, 看以下2个例子

# print(re.match("super", "superstition").span())
# 会返回(0, 5)
#
# 而
# print(re.match("super", "insuperable"))
# 则返回None
#
# search()会扫描整个字符串并返回第一个成功的匹配
# 例如：
# print(re.search("super", "superstition").span())
# 返回(0, 5)
#
# print(re.search("super", "insuperable").span())
# 返回(2, 7)

# NOTE 4, re.sub(pattern, repl, string, count=0, flags=0)

# 返回通过替换repl替换字符串中, 最左边不重叠的模式而获得的字符串。
#
# repl可以是字符串也可以是函数;
#
# 如果是一个字符串，反斜杠转义在其中被处理。
#
# 如果它是可调用的函数，则传递匹配对象并且必须返回要使用的替换字符串。
#
# (这解释看得有点模糊, 还是看下面的例子,容易理解) 简单来说就是个正则替换

# pattern, string, flags 就不解释了, 不懂的看上面

# repl，就是replacement，被替换，的字符串的意思。repl可以是字符串，也可以是函数。
# count 处理的次数

# demo

# 如果输入字符串是
# input_str = "hello 111 world 111"

# 你想替换 111 变成 222, 那么你可以通过字符串本身的替换方法
# replaced_str = input_str.replace("111", "222")

# 但是，如果输入字符串是
# input_str = "hello 123 world 456"

# 而你是想把123和456，都换成222 (以及其他还有更多的复杂的情况的时候), 那么就没法直接通过字符串的replace达到这一目的了。

# 就需要借助于re.sub，通过正则表达式，来实现这种相对复杂的字符串的替换
# replaced_str = re.sub("\d+", "", input_str)
# print(replaced_str)

# repl是函数的demo

# 比如输入内容是：hello 123 world 456
# 想要把其中的数字部分，都加上111，变成：hello 234 world 567

# count 参数, 控制替换的次数,范围

# def re_sub_demo():
#     input_str = "hello 123 world 456"
#
#     def add_numbers_in_input_str(matched):
#         int_str = matched.group("number")
#         return str(int(int_str) + 111)
#     # count 如果是1的话, 只处理前面的123, 默认是0(全部处理)
#     replaced_str = re.sub("(?P<number>\d+)", add_numbers_in_input_str, input_str, count=1)
#     print("input_str = %s, replaced_str = %s" % (input_str, replaced_str))
#
#
# re_sub_demo()

# NOTE 5, re.subn(pattern, repl, string, count=0, flags=0)

# 这个方法和re.sub基本类似, 只不过它返回一个元祖, (new_string, number)
# new_string 和 re.sub返回的一样, number表示统计subn方法处理过程中, 替换操作的次数

# NOTE 6, re.split(pattern, string, maxsplit=0, flags=0)

# 按照正则拆分源字符串，返回包含结果子字符串的列表。
# 如果正则中使用括号，则模式中所有组的文本也将作为结果列表的一部分返回。
# 如果maxsplit非零，则最多发生maxsplit拆分，并且字符串的其余部分将作为列表的最后一个元素返回。

# demo

# # 1.空格分
# test_str = 'w w w'
# print(re.split(r'[\s]', test_str))
#
# # 2.只分割一次
# print(re.split(r'[\s]', test_str, 1))
#
# # 3.多个字符分割
# test_str = 'w!w@w%w^w'
#
# print(re.split(r'[!@%^]', test_str))

# NOTE 7, re.findall(pattern, string, flags=0)

# 返回字符串中所有非重叠匹配的列表。

# 如果模式中存在一个或多个捕获组，则返回组列表;

# 如果模式有多个组，这将是一个元组列表。

# 结果中包含空匹配。

# demo

# #  + 是 匹配前一个一次或无数次
# # /s 是 匹配任何空白字符  这个demo中相当于空格
# # /w 是 匹配任何字母数字字符 这个demo中相当于a,b,c,d 这几个
#
# string = "a  b  c  d"
#
# # regex 中是带有2个括号的，我们可以看到其输出是一个list 中包含2个 tuple
# regex = re.compile("((\w)\s+\w)")
# print(regex.findall(string))
# # [('a  b', 'a'), ('c  d', 'c')]
#
# # regex 中带有1个括号，其输出的内容就是括号匹配到的内容，而不是整个表达式所匹配到的结果。
# regex1 = re.compile("(\w)\s+\w")
# print(regex1.findall(string))
# # ['a', 'c']
#
# # regex 中不带有括号,其输出的内容就是整个表达式所匹配到的内容。
# regex2 = re.compile("\w\s+\w")
# print(regex2.findall(string))
# # ['a  b', 'c  d']

# NOTE 8, re.finditer(pattern, string, flags=0)

# 在字符串中的所有非重叠匹配上返回迭代器。
# 对于每个匹配，迭代器返回一个匹配对象。
# 结果中包含空匹配。

# demo

# content = '''email:12345678@163.com
# email:2345678@163.com
# email:345678@163.com
# '''
#
# result_finditer = re.finditer(r"\d+@\w+.com", content)
# # 由于返回的为MatchObject的iterator，所以我们需要迭代并通过MatchObject的方法输出
# print(result_finditer)
# for i in result_finditer:
#     print(i.group())
#
# # finditer() 在提供匹配对象而不是字符串时很有用。
# # 如果想在某些文本中查找所有的副词及其位置, 他们将以下列方式使用 finditer():
# text = "He was carefully disguised but captured quickly by police."
# for m in re.finditer(r"\w+ly", text):
#     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

# NOTE 9, re.compile()

# 将正则表达式模式编译为正则表达式对象, 可用于使用其 match()、 search() 和其他方法进行匹配.
# 可以通过指定标志值来修改表达式的行为。值可以是下列任一变量, 并使用按位 or ( |运算符) 组合。

# 下面2行
# prog = re.compile(pattern)
# result = prog.match(string)

# 等效于
# result = re.match(pattern, string)

# 使用 re.compile() 并保存生成的正则表达式对象以供重用, 在单个程序中多次使用表达式时, 效率会更高

# NOTE 10, re.purge()

# 清除正则表达式缓存

# NOTE 11, template(pattern, flags=0)

# 编译模板模式，返回模式对象

# NOTE 12, re.escape()

# 除ASCII字母，数字和'_'外，转义模式中的所有字符。
