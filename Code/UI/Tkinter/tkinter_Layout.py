import tkinter as tk

# Tkinter 为我们提供了三个布局管理器：pack, grid 和 place

# pack, grid 和 place 均用于管理同在一个父组件下的所有组件的布局，其中：


# 1, pack 是按添加顺序排列组件

# 2, grid 是按行列形式排列组件

# 3, place 则允许程序员指定组件的大小和位置


# 对比 grid 管理器，pack 更适用于少量组件的排列，但它在使用上更加简单。
# 如果你需要创建相对复杂的布局结构，那么建议是使用多个框架（Frame）结构构成，或者使用 grid 管理器实现。

master = tk.Tk()

master.geometry("500x500+0+0")

# NOTE 注意：不要在同一个父组件中混合使用 pack() 和 grid()，因为 Tkinter 无法确定首先使用哪个布局管理器。

# 例如以下这个例子

# label_1 = tk.Label(bg="red", text="label_1")
# label_1.pack()
#
# label_2 = tk.Label(bg="green", text="label_2")
# label_2.grid()

# NOTE 1, pack 布局

# NOTE anchor

# 控制组件在pack分配的空间中的位置
#  "n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 "center" 来定位（ewsn 代表东西南北，上北下南左西右东）
# 默认值是 "center"

# label_1 = tk.Label(bg="red", text="label_1")
# label_1.pack()

# label_2 = tk.Label(bg="green", text="label_2")
# label_2.pack(anchor="w")

# NOTE expand

# 指定是否填充父组件的额外空间
# 默认值是 False

# NOTE fill

# 指定填充pack分配的空间
# 默认值是NONE，表示保持子组件的原始尺寸
# 还可以使用的值有：X（水平填充），Y（垂直填充）和BOTH（水平和垂直填充）
# 当GUI窗体大小发生变化时 X,Y,BOTH 设置后, widget在X、Y, BOTH方向跟随GUI窗体变化

# # 关于fill和expand的区别 看以下例子
# 将expand=0或者1切换对比, 或者在expand=0的情况下fill=tk.X或tk.Y之间对比
# tk.Label(master, text='Label', bg='green').pack(expand=1, fill=tk.X)
# tk.Label(master, text='Label2', bg='red').pack(fill=tk.BOTH)

# 个人理解expand类似于控件的外边距(透明)那样填充父控件的位置
# fill就是控件内部所占的空间扩容

# TODO in_ (待验证)

# 将该组件放到该选项指定的组件中
# 指定的组件必须是该组件的父组件

# NOTE ipadx, ipady
# 指定水平,竖直方向上的内边距

# label_2 = tk.Label(bg="green", text="label_2")
# label_2.pack(ipady="20", ipadx="30")

# NOTE padx, pady
# 指定水平,竖直方向上的外边距

# label_1 = tk.Label(bg="red", text="label_1")
# label_1.pack()
# label_2 = tk.Label(bg="green", text="label_2")
# label_2.pack(pady="30")

# NOTE side

# 指定组件的放置位置
# 默认值是TOP
# 还可以设置的值有：LEFT，BOTTOM，RIGHT

# label_2 = tk.Label(bg="green", text="label_2")
# label_2.pack(side=tk.LEFT)

# NOTE def pack_configure(self, cnf={}, **kw):

# cnf 参数字典
# **kw 参数用法和pack一样

# label_2 = tk.Label(bg="green", text="label_2")
# label_2.pack_configure(cnf={"side": tk.LEFT})

# NOTE def pack_forget(self):

# 将组件从屏幕中隐藏
# 并没有销毁该组件，只是看不到了
# 可以通过 pack 或其他布局管理器显示已隐藏的组件

# label_1 = tk.Label(bg="red", text="label_1")
# label_1.pack_forget()
#
# label_2 = tk.Label(bg="green", text="label_2")
# label_2.pack()
#
# # 再显示
# label_1.pack()

# NOTE def pack_info(self):

# 以字典的形式返回当前 pack 的选项

# label_2 = tk.Label(bg="green", text="label_2")
# label_2.pack()
# print(label_2.pack_info())

# NOTE pack_propagate(flag)

# 如果开启，父组件会自动调节尺寸以容纳所有子组件
# 默认值是开启（flag = True）
# 该方法仅适用于父组件

# frame = tk.Frame(master, width=400, height=400, bg='green')
#
# # 将框架放在其父级中
# frame.pack()
#
# # 告诉框架不要让它的子控件控制它的大小(可以切换0或1看效果)
# frame.pack_propagate(0)
#
# # 将文本框放在框架中
# textBox = tk.Label(frame, text="(x,y): ", bg='red')
# textBox.pack()

# NOTE pack_slaves()

# 以列表的形式返回该组件的所有子组件

# label_2 = tk.Label(bg="green", text="label_2")
# label_2.pack()
# print(master.pack_slaves())


# NOTE 2, grid布局

# NOTE column, row

# 指定组件插入的列, 行（0 表示第 1 列, 行）
# 默认值是 0

# label_1 = tk.Label(bg="green", text="label_1")
# label_1.grid(column=0)
#
# label_2 = tk.Label(bg="green", text="label_2")
# label_2.grid(column=1)  # 如果这里是2 只是代表一个左右, 上下的关系 并不是再空一列, 行

# TODO columnspan(没懂) or rowspan(没懂)

# 指定用多少列（跨列）显示该组件
# 组件的列宽
# 从组件所置单元格算起在列方向上的跨度；

# label_1 = tk.Label(master, text="label_1", bg='red')
# label_1.grid(row=0, column=0, rowspan=2, columnspan=2)
#
# label_2 = tk.Label(master, text="label_2", bg='green')
# label_2.grid(row=0, column=1)
#
# label_3 = tk.Label(master, text='label_3', bg='blue')
# label_3.grid(row=1, column=0)

# NOTE sticky

# 默认的控件在窗口中的对齐方式是居中。
# 可以使用sticky选项去指定对齐方式，可以选择的值有：N/S/E/W，
# 分别代表上对齐/下对齐/左对齐/右对齐，可以单独使用N/S/E/W，也可以上下和左右组合使用，达到不同的对齐效果，如

# from tkinter import *
#
# label_1 = tk.Label(master, text='First', height=3, width=7, bg='red')
# label_2 = tk.Label(master, text='Second', height=6, width=13, bg='blue')
#
# # 2个控件 竖直排布
# # label_1.grid(sticky=E + W)  # 1, 左右都对齐
# # label_1.grid(sticky=E)  # 2, 左对齐
# # label_1.grid(sticky=W)  # 3, 右对齐
# # label_1.grid()  # 4, center
#
# # 2个控件 水平排布
# # label_1.grid(sticky=N + S)  # 1, 上下都对齐
# # label_1.grid(sticky=N)  # 2, 上对齐
# # label_1.grid(sticky=S)  # 3, 下对齐
# # label_1.grid()  # 4, center
#
# label_2.grid(row=0, column=1)

# 还有其它组合自己尝试

# NOTE

master.mainloop()
