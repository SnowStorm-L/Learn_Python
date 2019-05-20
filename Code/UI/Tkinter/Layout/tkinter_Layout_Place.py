import tkinter as tk

master = tk.Tk()

master.geometry("500x500+0+0")

test_label = tk.Label(text='text', bg='red')

# NOTE Place 布局

# NOTE Place and place_configure

# def place_configure(self, cnf={}, **kw):

# cnf 参数字典
# **kw 参数用法和grid一样

# NOTE x y

# 指定该组件的起始点水平(竖直)偏移位置（像素）
# 如同时指定了 relx(rely) 选项，优先实现 relx(rely) 选项

# test_label.place(x=30, y=30)  # relx=0.6, rely=0.8

# NOTE relx rely

# 指定该组件的起始点相对于父组件的水平(竖直)位置
# 取值范围 0.0 ~ 1.0

# test_label.place(relx=0.9, rely=0.9)

# NOTE in in_

# 参考 Pack 的in_ 用法

# NOTE width height

# 此小部件的宽度(高度)以像素为单位

# test_label.place(width=30, height=40)

# NOTE relwidth relheight

# 相对于master的宽度(高度)，此小部件的宽度(高度)在0.0到1.0之间（1.0与master的宽度(高度)相同）

# test_label.place(relwidth=0.5, relheight=0.1)

# NOTE bordermode

# 指定边框模式（"inside" 或 "outside"）
# 默认值是 "inside"

# f1 = tk.Frame(borderwidth=5, relief=tk.SUNKEN, width=50, height=50)
# f1.pack()
#
# l1 = tk.Label(f1, text="Hi")
# l1.place(x=10, y=10, bordermode="outside")
#
# f2 = tk.Frame(borderwidth=5, relief=tk.SUNKEN, width=50, height=50)
# f2.pack()
#
# l2 = tk.Label(f2, text="Hi")
# l2.place(x=10, y=10, bordermode="inside")

# NOTE anchor

# 基于原有位置基础上的偏移

# 可设置选项为 n, ne, e, se, s, sw, w, nw, or center

# 默认值是 "nw" 西北

# 上北下南,左西右东

# 东：E 源于east
# 南：S 源于south
# 西：W 源于west
# 北：N 源于north

# test_label.place(x=30, y=40, anchor="se")
#
# tk.Label(text='text', bg='green').place(x=30, y=40)  # 这个是不设置anchor 之前做对比的

master.mainloop()
