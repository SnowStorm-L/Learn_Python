import tkinter as tk

master = tk.Tk()

master.geometry("500x500+0+0")

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

# NOTE in_

# 将该组件放到该选项指定的组件中
# 指定的组件必须是该组件的父组件

# f1 = tk.Frame(width=200, height=200, background="red")
# f2 = tk.Frame(width=100, height=100, background="blue")
#
# f1.pack(fill="both", expand=False, padx=20, pady=20)
# f2.place(in_=f1, anchor="c", relx=.5, rely=.5)  # 加了in_之后 f2在f1中心,  不加in_f2在master中心

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

master.mainloop()
