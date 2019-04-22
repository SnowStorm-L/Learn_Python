#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 PM4:47
# @Author  : L
# @Email   : L862608263@163.com
# @File    : const.py
# @Software: PyCharm

import sys


class Const(object):
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError('Constants can`t be modified')
        if not name.isupper():
            raise TypeError('Constant names must be capitalized')
        self.__dict__[name] = value


sys.modules[__name__] = Const()

# from project.utils import const

# import const

# const.USER_ID = "123132"
