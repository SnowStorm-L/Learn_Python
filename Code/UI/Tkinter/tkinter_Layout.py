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

# NOTE pack 布局

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

label_2 = tk.Label(bg="green", text="label_2")
label_2.pack(side=tk.LEFT)


master.mainloop()
