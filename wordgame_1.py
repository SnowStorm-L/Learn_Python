import random

print('----------')
print("转\"义\"引号")

temp = input("请输入一个数字: ")
guess = int(temp)

# type 获取数据类型
print(type(temp))
# 返回布尔,判断类型是否一致
print(isinstance(temp, int))

result = random.randint(0, 5)

guessTime = 3

# 缩进表示内容在if内
if result == guess:
    print("猜对了")
elif result > guess:
    print("猜小了")
else:
    print("猜大了")

guessTime -= 1

while result != guess and guessTime > 0:
    temp = input("请输入一个数字: ")
    guess = int(temp)
    result = random.randint(0, 5)
    guessTime -= 1
    if result == guess:
        print("猜对了")
        break
    elif result > guess:
        print("猜小了")
    else:
        print("猜大了")

print("游戏结束 结果是" + str(result))

# and 逻辑操作符  可以将任意表达式连接在一起 并得到一个布尔类型的值

# e记法 e是10 e后面是次方的意思 e后面加(+,-) 正负多少次方

lalala = 15e10

print(lalala)

# 类型转换

str()
float()
# 截断处理 小数后面扔了 int(5.99) 结果5
int()

# 使用内建函数命名  会使内建函数失效
# str = "111"
#
# print(str(5))


#   BIF 全称 Build In Functions (内建函数)
#  控制台输入 dir(__builtins__) 查看内建函数(小写的都是,其它不知道)
#  help(xxx)  查看内建函数的作用解释

# 字符串前面加个r  强制不转义
# 原始字符串结尾加\  后面"\\"
path = r"C:\now""\\"

print(path)

# 反斜杠转义
Cpath = "C:\\aaa"

print(Cpath)

# 多行字符串
MultiLineString = """
                     第一行
                     第二行
                     第三行
                  """

print(MultiLineString)

# 算术运算符 + - * / %  **  //

# 全部赋值
# a = b = c = d = 10

# //和/的区别

# / "就一定表示 浮点数除法，返回浮点结果;"
# // "表示向下取整(小数全砍掉,除数或被除数有.0f的结果也带.0)除法。

# a = 5
# b = 2.3
#
# print(a//b)

# **幂运算
#
# a = 5
# b = 2
#
# 5的2次方
# print(a**b)

# 逻辑操作符  and(&&) or(||) not(取相反布尔类型值 bool = !bool )

# 悬挂else问题

# if ( hi > 2 )
#     if ( hi > 7)
#         printf()
# else
#     printf()

# 以上代码在C中 else是就近匹配原则 这个else 是 hi > 7 的 else

# 在python中不同  else是以对齐方式(缩进级别) 如果是python 这个else 就是 hi > 2 的 else

# 条件表达试(三元操作符)

# x, y = 4, 5
# if x < y:
#     small = x
# else:
#     small = y

# 以上代码可以缩写为

# (为真的结果)if(条件)else(为假的结果)
# 其它语言写法 small = x < y ? x : y
# small = x if x < y else y

# 断言(当后面条件为假的时候) 抛出AssertionError的异常警告
# assert 3 > 4

# 循环
# while, for
#
# forStr = "12345"
# member = [1, 2, 3, 4] 数组
# for idx in forStr:
#     print(idx, len(idx) #计算参数长度)

# 区间range()
# range( [start,] stop[, step = 1] )
#
# 这个BIF有三个参数,其中用中括号括起来的两个表示可选参数
# step = 1 表示第三个参数的默认值是1
# range这个BIF的作用是生产一个从start参数的值开始到stop参数的值结束的数字序列

# range(5)
# list(range(5)) 结果 [0,1,2,3,4]

# range(2, 9)
# list(range(2, 9)) 结果 [2 , 3, 4, 5, 6, 7, 8] 不包含9

# range(1, 10 , 2) 第三个参数2是步进
# 结果 [1, 3, 5, 7, 9] 每次递增2

# break 终止当前循环体, continue 跳出本次循环体

for idx in range(10):
    if idx%2 != 0:
        print(idx)
        continue
    idx += 2
    print(idx)


