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

master.mainloop()
