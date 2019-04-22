#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 11:14 AM
# @Author  : L
# @Email   : L862608263@163.com
# @File    : tkinter_Label.py
# @Software: PyCharm

import tkinter as tk

# 标签小部件，可以显示文本和位图。

master = tk.Tk()

master.title("TK title 属性")

master.geometry("300x600+0+0")

# NOTE Label（master=None, cnf={}, **kw）

# 标准选项

"""
activebackground, 
activeforeground, 
anchor,
background, 
bitmap, 
borderwidth, 
cursor,
disabledforeground, 
font, 
foreground,
highlightbackground, 
highlightcolor,
highlightthickness, 
image, 
justify,
padx, 
pady, 
relief, 
takefocus, 
text,
textvariable, 
underline, 
wraplength
"""

# 特定于WIDGET的选项

"""
 height, state, width
"""

# 其中，kw参数是用来自定义lable组件的键值对。

# cnf必须是将选项名称映射到值的配置字典。
# 它可以通过位置或名称传递（但不能同时传递！）。
# 当多个小部件具有一组通用选项时，这非常有用。
# 选项也可以传递（通过关键字），个别选项覆盖dict中的任何选项。

cnf = {"text": "cnf_label", 'bg': 'red'} # 对于多个label, 同样的样式, 作归纳配置使用

cnf_label = tk.Label(master, cnf= cnf)
cnf_label.pack() # 添加到视图上

# NOTE 1,2  activebackground, activeforeground 这2个属性对于Label不知道有什么作用

label_1 = tk.Label(master,
                 activebackground = "red", #
                 activeforeground = "green",
                 text = "label_1",
                 bg = "yellow"
                 )
label_1.pack()

# NOTE 3, anchor 控制文本（或图像）在 Label 中显示的位置

# "n", "ne",
# "e", "se",
# "s", "sw",
# "w", "nw", 或者 "center" 来定位
# （ewsn 代表东西南北，上北下南左西右东）
# 默认值是 "center"

label_2 = tk.Label(master, anchor = "e", text = "label_2", width = "100", bg = "red")

label_2.pack()

# NOTE 4, background 可简写为bg 设置背景色

# NOTE 5, bitmap

# TODO bitmap 能否用自定义的图片?

# 指定显示到label上的位图
# 如果指定了image，则该选项忽略

# 内置的图片

"""
* error
* hourglass
* info
* questhead
* question
* warning
* gray12
* gray25
* gray50
* gray75
"""

label_3 = tk.Label(master, width = "100", bitmap = "error", bg = "green")

label_3.pack()

# NOTE 6, borderwidth (不加relief看不到效果)

# 指定 Label 的边框宽度
# 默认值由系统指定，通常是 1 或 2 像素

label_4 = tk.Label(master, text = "label_4", borderwidth = "5", relief="groove")

label_4.pack()

# NOTE 7, cursor

# 指定当鼠标在 Label 上飘过的时候的鼠标样式
# 默认值由系统指定

# 具体样式能否显示, 与平台相关(有些只能用在mac上, 有些只能用着win上)
"arrow"
"circle"
"clock"
"cross"
"dotbox"
"exchange"
"fleur"
"heart"
"man"
"mouse"
"pirate"
"plus"
"shuttle"
"sizing"
"spider"
"spraycan"
"star"
"target"
"tcross"
"trek"
"watch"

label_5 = tk.Label(master, text = "label_5", cursor = "heart")

label_5.pack()

# NOTE 8, disabledforeground

# 指定当 Label 不可用的时候前景色的颜色
# 默认值由系统指定

label_6 = tk.Label(master, text = "label_6", state = "disabled", disabledforeground = "red")

label_6.pack()

# NOTE 9, font

# 指定 Label 中文本的字体(注：如果同时设置字体和大小，应该用元组包起来，如（"楷体", 20）
# 一个 Label 只能设置一种字体
# 默认值由系统指定

from tkinter.font import Font

test_font = Font(size = 44)

# label_7 = tk.Label(master, text = "label_7", font = ("Courier", 44, "bold"))
label_7 = tk.Label(master, text = "label_7", font = test_font)

label_7.pack()

# NOTE 10, foreground 可简写为fg

# 设置 Label 的文本和位图的前景色颜色
# 默认值由系统指定

label_8 = tk.Label(master, text = "label_8", foreground = "red") # , bitmap = "error"

label_8.pack()

# NOTE 11, highlightbackground

# NOTE 12, highlightcolor

# NOTE 13, highlightthickness

label_9 = tk.Label(master, text = "label_9", highlightcolor = "red", relief = "ridge")
label_9.focus_set()
label_9.pack()

# print(label.config()) 打印设置属性

master.mainloop()


