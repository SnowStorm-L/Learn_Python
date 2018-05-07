#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 AM11:04
# @Author  : L
# @Email   : L862608263@163.com
# @File    : exception.py
# @Software: PyCharm

# py官网文档异常解释
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning

# 异常处理

# try:
#     检测范围
# except Exception as reason:  (as reason 是帮异常取别名,可选)
#     出现异常(Exception)后的处理代码
# finally:
#     无论异常与否都执行的代码(例如try里面open一个file, 就要在finally里面close)

array = [1, 2]

try:
    print(array[3])

    # 如果try里面有多个语句异常
    # 例如
    # array[4]
    # array[5]
    # 那只走第一个异常并抛出错误,其它后面的异常不走

except Exception as array_error_reason:
    print('错误类型是:', type(array_error_reason))
    print('错误原因是: ', array_error_reason)
# except TypeError: 可以except不同类型异常分别处理
# except (TypeError, OSError): 也可以一起处理

# raise 引发异常
raise ZeroDivisionError('自己的异常')
