#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 PM3:46
# @Author  : L
# @Email   : L862608263@163.com
# @File    : easy_gui.py
# @Software: PyCharm

# 安装easyGUI

# command + , 进入 preference
# 输入interpreter
# 输入库名 install package

# 导入方法1

# import easygui

# 如果使用上面这种形式导入的话,那么使用EasyGui的函数的时候,必须在函数的前面加上前缀easygui
# 例如 easygui.msgbox()

# 导入方法2

# from easygui import *

# 这使得我们更容易调用EasyGui的函数,但是有其它问题,例如你导入的库的函数名msgbox与你本类的方法名重复了,会覆盖掉
# 例如 msgbox()

# 导入方法3
# 这种方法比较推荐,既能保持easygui的命名空间,又能减少前缀的代码数

import easygui as g

g.msgbox(title='你妈嗨')
