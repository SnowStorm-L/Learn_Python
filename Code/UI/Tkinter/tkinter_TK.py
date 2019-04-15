#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 6:02 PM
# @Author  : L
# @Email   : L862608263@163.com
# @File    : tkinter_TK.py
# @Software: PyCharm


from tkinter import  *
from Code.Tools.l_log import *

# Tk的顶级小部件，主要代表应用程序的主窗口。(根窗口)

# TK 这个类继承于 Wm和Misc, class Tk(Misc, Wm):

tk = Tk(className="123")

# NOTE Wm介绍(提供与窗口管理器通信的功能。)

# NOTE 注：并非所有操作系统均完全支持下方所有方法的实现。

# NOTE 1, wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
# 控制该窗口的宽高比（width:height）
# 宽高比限制在：minNumer / minDenom ~ maxNumer / maxDenom
# 如果忽略参数，则返回一个 4 元组表示当前的限制（如果有的话）

l_log(tk.aspect())
# tk.aspect(minNumer=1, minDenom=1, maxNumer=1, maxDenom=1)
# l_log(tk.aspect())

# NOTE 2, wm_attributes(self, *args):
# 设置和获取窗口属性
# 如果你只给出选项名，将返回当前窗口该选项的值

# https://wiki.tcl-lang.org/page/wm+attributes

# NOTE 以下选项不支持关键字参数，你需要在选项前添加横杠（-）并用字符串的方式表示，用逗号（,）隔开选项和值。
# 例如你希望设置窗口的透明度为 50%，你应该使用 attribute("-alpha", 0.5) 而不是 attribute(alpha=0.5)

# ('-alpha', 1.0, '-fullscreen', 0, '-modified', 0, '-notify', 0, '-titlepath', '', '-topmost', 0, '-transparent', 0)
l_log(tk.attributes())

# 1, -alpha double
# (Windows，Mac)控制窗口的透明度, 1.0 表示不透明，0.0 表示完全透明, 该选项并不支持所有的系统.
# 对于不支持的系统，Tkinter 绘制一个不透明（1.0）的窗口

# tk.attributes("-alpha", 0.5)

# 2, -disabled boolean
# （Windows）禁用整个窗口（这时候你只能从任务管理器中关闭它）

# 3, -fullscreen boolean
# （Windows，Mac）如果设置为 True，则全屏显示窗口

# tk.attributes("-fullscreen", True)

# 4, modified boolean
# （Mac）如果设置为 True，该窗口被标记为改动过

# FIXME 没看懂
# 5, titlepath
# （Mac）将（可拖动）文件图标与可用于与其他应用程序管理给定文件的窗口标题相关联

# tk.attributes("-titlepath", "/Users/l/Desktop/Resource/Swift.png")

# 6, -toolwindow boolean
# （Windows）如果设置为 True，该窗口采用工具窗口的样式
# 在标题栏的右侧创建一个带有单个关闭按钮（比平常小）的窗口

# 7, -topmost boolean
# （Windows，Mac）如果设置为 True，该窗口将永远置于顶层

# tk.attributes("-topmost", True)

# 8, -transparent boolean
# (Mac)控制窗口是否有阴影
# 对透明窗口有用，但必须小心谨慎以便利用

# 9, -notify boolean
# (Mac) 控制窗口图标是否在停靠栏中弹跳 (启动程序后在dock栏跳一下)

# tk.attributes("-notify", False)

# 10, -zoomed boolean
# (Unix/X11 Attributes)控制此窗口是否处于缩放状态

# 11, -type list
# (Unix/X11 Attributes)

# 这在Tk 8.6,8.5.9 +和8.4.20+中提供，以支持扩展窗口管理器提示属性，该属性管理X11上的顶层窗口类型。
# 适当地设置它可以允许窗口管理器应用相关的样式和动画。
# 例如，工具提示窗口可能具有在映射和取消映射工具提示时使用的动画。
# Combobox下拉列表具有与对话框不同的样式。 此属性的值应设置为首选窗口类型列表，因为并非所有窗口管理器都支持所有类型。

# NOTE title
tk.title("TK title 属性") # 修改框体的名字,也可在创建时使用className参数来命名；

# NOTE resizable
# 是否可以手动拉伸window的宽高。
# 两个值都是布尔值。

# FIXME (不设置窗口可拉伸最大,最新范围的情况下  拉伸后黑屏? 单一方向禁止拉伸无效?)
tk.resizable(True, True) # 或者写0 or 1

# NOTE geometry
# 设置窗口的位置,大小

# 参数结构为  width x height + x + y。
# 如果给出None，则返回当前值。
tk.geometry("250x100+300+40")

# 设置窗口可拉伸的最大 宽度, 高度
# tk.maxsize(width=300, height=200)

# 设置窗口可拉伸的最小 宽度, 高度
# tk.minsize(width=10, height=10)

l_log(tk.state())

mainloop()
