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

master.title("TK Label 学习")

master.geometry("300x800+0+0")

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
compound
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

cnf = {"text": "cnf_label", 'bg': 'red'}  # 对于多个label, 同样的样式, 作归纳配置使用

cnf_label = tk.Label(master, cnf=cnf)
cnf_label.pack()  # 添加到视图上

# TODO 1,2  activebackground, activeforeground

# 用于设置Label处于活动（active）状态下的背景和前景颜色,默认由系统指定。

label_1 = tk.Label(master,
                   activebackground="yellow",
                   activeforeground="green",
                   text="label_1",
                   state="active"
                   )
label_1.pack()

# NOTE 3, anchor 控制文本（或图像）在 Label 中显示的位置

# "n", "ne",
# "e", "se",
# "s", "sw",
# "w", "nw", 或者 "center" 来定位
# （ewsn 代表东西南北，上北下南左西右东）
# 默认值是 "center"

label_2 = tk.Label(master, anchor="e", text="label_2", width="100", bg="red")

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

label_3 = tk.Label(master, width="100", bitmap="error", bg="green")

label_3.pack()

# NOTE 6, borderwidth 简写 bd (不加relief看不到效果)

# 指定 Label 的边框宽度
# 默认值由系统指定，通常是 1 或 2 像素

label_4 = tk.Label(master, text="label_4", bd="5", relief="groove")

label_4.pack()

# NOTE 7, cursor

# 指定当鼠标在 Label 上飘过的时候的鼠标样式
# 默认值由系统指定

# 具体样式能否显示, 与平台相关(有些只能用在mac上, 有些只能用着win上)
'''
arrow 箭头
based_arrow_down 基础向上箭头
based_arrow_up 基础向下箭头
mouse 鼠标
boat 船
pencil 铅笔
bogosity 虚假度
bottom_left_corner 左下角
bottom_right_corner 右下角
question_arrow 问题箭头
bottom_side 最下边
right_ptr 右指针
bottom_tee T型底
right_side 最右边
box_spiral 方螺旋
right_tee T型右
center_ptr 中指针
circle 圆
clock 表
sailboat 帆船
coffee_mug 咖啡杯
sb_down_arrow 宽下箭头
cross 十字
sb_h_double_arrow 宽水平双箭头
cross_reverse 米字
sb_left_arrow 宽左箭头
crosshair 十字线
sb_right_arrow 宽右箭头
diamond_cross 十字钻
sb_up_arrow 宽上箭头
dot 点
sb_v_double_arrow 宽垂直双箭头
dotbox 方点
shuttle 梭子型
double_arrow 双箭头
sizing 改变大小
draft_large 大拖拽
spider 蜘蛛
draft_small 小拖拽
spraycan 喷枪
draped_box 褶皱盒子
star 星星
exchange 交换
target 目标
fleur 十字花
tcross T型十字
gobbler 火鸡
top_left_arrow 左上箭头
gumby gumby（卡通角色
hand1 手型1
top_right_corner
hand2 手型2
top_side 最上边
heart 心型
top_tee T型上
icon 图标
trek 跋涉
iron_cross 铁十字
ul_angle 左上角度
left_ptr 左指针
umbrella 雨伞
left_side 最左边
ur_angle 右上角度
left_tee T型左
watch 表
leftbutton
xterm 输入光标
ll_angle 左下角度
X_cursor X型指针
lr_angle 右下角度
'''

label_5 = tk.Label(master, text="label_5", cursor="bogosity")

label_5.pack()

# NOTE 8, disabledforeground

# 指定当 Label 不可用的时候前景色的颜色
# 默认值由系统指定

label_6 = tk.Label(master, text="label_6", state="disabled", disabledforeground="red")

label_6.pack()

# NOTE 9, font

# 指定 Label 中文本的字体(注：如果同时设置字体和大小，应该用元组包起来，如（"楷体", 20）
# 一个 Label 只能设置一种字体
# 默认值由系统指定

from tkinter.font import Font

test_font = Font(size=44)

# ('Times',10,'bold','italic')    依次表示字体、字号、加粗、倾斜
# label_7 = tk.Label(master, text = "label_7", font = ('Times',10,'bold','italic'))
label_7 = tk.Label(master, text="label_7", font=test_font)

label_7.pack()

# NOTE 10, foreground 可简写为fg

# 设置 Label 的文本和位图的前景色颜色
# 默认值由系统指定

label_8 = tk.Label(master, text="label_8", foreground="red")  # , bitmap = "error"

label_8.pack()

# TODO 11, highlightbackground

# 指定当Label没有获得焦点时的高亮边框颜色

# TODO 12, highlightcolor

# 当Label获得焦点时的高亮边框颜色

# TODO 13, highlightthickness

# 指定高亮边框的宽度
# 默认值是0

label_9 = tk.Label(master,
                   text="label_9",
                   highlightcolor="yellow",
                   highlightbackground="red",
                   highlightthickness=5)
# 设置焦点(当TK主窗口获得焦点时, 边框显示黄色, 当PyCharm获得焦点时, 边框显示红色)
# 上面这3个参数 仅在Label允许接收焦点的情况下 才能看到切换变化
# label_9.focus_force()  # 不加这行看不到切换变化
label_9.pack()

# NOTE 11, image

# 指定 Label 显示的图片
# 该值应该是 PhotoImage，BitmapImage，或者能兼容的对象
# 该选项优先于 text 和 bitmap 选项 (当设置image选项时, bitmap选项设置失效)

# 你可以使用 Label 显示 PhotoImage 和 BitmapImage 对象。
# 当你这么做的时候，请务必保留一份图片对象的引用，以防止被 Python 的垃圾回收机制回收。
# 你可以使用一个全局变量，或一个实例的属性，或者再简单点，在实例上添加一个属性即可：

image_path = "../Resources/strlen.gif"

gif_frames = 59

image = tk.PhotoImage(file=image_path)

label_10 = tk.Label(master, image=image)

frames = [tk.PhotoImage(file=image_path, format='gif -index %i' % (i)) for i in range(gif_frames)]


def update(idx):
    frame = frames[idx]
    idx += 1
    label_10.configure(image=frame)
    master.after(100, update, idx % gif_frames)


label_10.pack()

master.after(0, update, 0)

# NOTE 12, justify

# 定义如何对齐多行文本
# 使用 "left"，"right" 或 "center"
# 注意，文本的位置取决于 anchor 选项
# 默认值是 "center"

# NOTE 13, 14 padx, pady

# 指定 Label 水平(竖直)方向上的额外间距（内容和边框间）

label_11 = tk.Label(master, text="label_11", bd="2", relief="groove", padx="5", pady="20")

label_11.pack()

# NOTE 15, relief

# 指定边框样式
# 默认值是 "flat"
# 另外你还可以设置 "groove", "raised", "ridge", "solid" 或者 "sunken"

# TODO 16, takefocus (待验证)

# 如果是 True，该 Label 接受输入焦点
# 默认值是 False

label = tk.Label(master, text="good good study", bg="red", takefocus=True)
# 设置焦点
# label.focus_set()
# 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '0', '0')
print(label.config())
label.pack()


def func(event):
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)


# <Key> 响应所有的按键

label.bind("<Key>", func)

# NOTE 17, text

# 指定 Label 显示的文本
# 文本可以包含换行符
# 如果设置了 bitmap 或 image 选项，该选项则被忽略

# NOTE 18, textvariable

# Label 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容
# 如果变量被修改，Label 的文本会自动更新


# 一个倒计时的例子

remaining = 0

prompt = tk.StringVar()


def snooze(secs):
    """
    Snoozes for the given number of seconds. During the snooze, a progress
    dialog is launched notifying the
    """

    def decrement_label():
        global remaining, prompt
        remaining -= 1
        prompt.set('Snoozing %d sec(s)' % remaining)
        label.update_idletasks()
        if not remaining:
            prompt.set("end")

    global remaining
    prompt.set("start")
    label = tk.Label(master, textvariable=prompt, width=30, bg='purple')
    label.pack()

    remaining = secs
    for i in range(1, secs + 1):
        master.after(i * 1000, decrement_label)


snooze(20)

# NOTE 19, underline

# 跟 text 选项一起使用，用于指定哪一个字符画下划线（例如用于表示键盘快捷键）
# 默认值是 -1

label_12 = tk.Label(master, text="label-12", underline=1)

# 如果需要underline所有字符串
# f = Font(label_12, label_12.cget("font"))
# f.configure(underline=True)
# label_12.configure(font=f)

label_12.pack()

# NOTE 20, wraplength

# 决定 Label 的文本应该被分成多少行
# 该选项指定每行的长度，单位是屏幕单元
# 默认值是 0

label_13 = tk.Label(master, text="label_13", wraplength=20, bg="orange")

label_13.pack()

# NOTE 21, compound

# 控制 Label 中文本和图像的混合模式
# 默认情况下，如果有指定位图或图片，则不显示文本
# 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）
# 如果该选项设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边（如 "bottom"，则图像在文本的下方）
# 默认值是 NONE


label_14 = tk.Label(master, text="label_14", height="100", image=image, compound="right", bg="yellow")

label_14.pack()

# print(label.config()) 打印设置属性

# NOTE 22, state

# 指定 Label 的状态
# 这个标签控制 Label 如何显示
# 可设置的选项为: normal(默认)/active/disable

# NOTE 23, 24 width, height

# 设置 Label 的宽度(高度)
# 如果 Label 显示的是文本，那么单位是文本单元
# 如果 Label 显示的是图像，那么单位是像素（或屏幕单元）
# 如果设置为 0 或者干脆不设置，那么会自动根据 Label 的内容计算出宽度(高度)

master.mainloop()
