#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# 列表、元组和字符串的共同点
# - 都可以通过索引得到每一个元素
# - 默认索引值总是从0开始
# - 可以通过分片的方法得到一个范围内的元素的集合
# - 有很多共同的操作符(重复操作符、拼接操作符、成员关系操作符)

# list()
# 把一个可迭代对象转换为列表

# 迭代
# 重复反馈过程的活动,其目的是为了接近所需目标或结果
# 每一次对过程的重复称为一次“迭代”，而每一次迭代得到的结果会作为下一次迭代的初始值。

emptyList = list()

strList = list('python learn')

tupleList = list((1, 1, 2, 3, 5, 8, 13, 21, 34))

# tuple()
# 把一个可迭代对象转换为元组

print(len(tupleList))

print(max(tupleList))

print(min(tupleList))

# sum 后面有个可选值 sum(p1, p2) 计算完p1的结果后再加上p2
print(sum(tupleList))

# reversed 返回一个迭代器对象
print(list(reversed(tupleList)))

# 枚举
# 返回元组,  下标和数据
print(list(enumerate(tupleList)))

zipA = [1, 2, 3]
zipB = [4, 5, 6, 7]
# 成对打包,多出的扔掉
print(list(zip(zipA, zipB)))

stringArray = ['a', 'b', 'c', 'd']
numberArray = [1, 2, 3, 4]
mixArray = [1, 'a', 3.14, [1, 2, 3]]

# 创建空list又加值得话,pycharm会检查,并建议直接设置一个有值的list
emptyArray = []
emptyArray.append('美羊羊')

# 修改, 注意不能越界
emptyArray[0] = '有角'

# 多个添加
emptyArray.extend(['公羊', '才有角'])

# 按下标插入
emptyArray.insert(0, '美羊羊')

print(emptyArray)

# 下标获取值
# print(emptyArray[1])

# 删除List元素, 确保在List里面才行, 乱删的话会报错
# emptyArray.remove('积极')

# 删除List下标元素,或整个列表(下标不能越界)
# del emptyArray[9]

# 删除List元素, 不带参数就是弹出最后一个元素, 带参数可以弹出下标参数 -> pop(index)
# emptyArray.pop()


# 列表切片
#  :后面那个数字 是索引结束位置，即不包括索引为2的元素
#  如果开始索引为0，还可以省略, 结束索引不写的话,默认到结尾
print(emptyArray[:2])

# Python取元素还支持emptyArrayL[-1]这种取倒数第一个元素的操作
# print(emptyArray[-2:-1])
# print(emptyArray[:-1])
# print(emptyArray[-2:])

# [:] 这个表示复制一个list，其实就是默认把整个list切片。

listOne = [123]
listTwo = [234]

# 会比较其中元素大小 结果 False
print(listOne > listTwo)

listOne.append(456)
listTwo.append(123)

# 结果False 只管第一个元素的结果,后面元素不比较
print(listOne > listTwo)

listThree = listOne

print(listOne < listTwo and listOne == listThree)

# 拼接
listFour = listOne + listTwo
# + 号两边类型必须一致, 不能实现以下操作
# listFour + '咳咳'
# print(listFour)
#
# print(listFour * 2)
#
# listFour *= 5
# print(listFour)

# 判断List是否存在元素 in 和 not in
# ***注意,不能判断多维数组 [[], []] 中的元素 除非指定层数 in listFour[0]
print(123 in listFour)
print(123 not in listFour)

# count 元素出现在List的次数
print(listFour.count(123))

# 返回第一个123元素, 属于区间内的下标(后面有再多个也不管)
# 下标0到20的区间
print(listFour.index(123, 0, 20))

print(listFour)

# List元素反转
listFour.reverse()

print(listFour)

# 排序(默认重小到大)
listFive = [0, 4, 2, 1, 3]

# sort有三个参数 sort(func, key, reverse=False)
# 排序的算法,算法的关键字,reverse是否翻转默认False
listFive.sort()

print(listFive)

# 列表推导式或列表解析

# 列表推导式（List comprehensions）也叫列表解析，灵感取自函数式编程语言 Haskell。Ta 是一个非常有用和灵活的工具，可以用来动态的创建列表
#
# 语法如：
# [有关变量的表达式 for 变量 in 列表] 或者 [有关变量的表达式 for 变量 in 列表 if 条件]

print([i*i for i in range(10) if i % 3 == 0])

# 上面的写法相当于以下的代码

# list1 = []
# for x in range(10):
#     list1.append(x**2)

# 相关的也有 字典推导,集合推导...

# 字典
print({x: x > 3 for x in range(10)})

# 集合
print({x for x in range(10)})

# *** 重点  为什么要用[:]重新切片(拷贝)整个数组, 而不用newList = originList
# 看以下例子

# 感觉像是 等号左边的标签指向右边

# python中的对象之间赋值时是按**引用传递**的，如果需要拷贝对象，需要使用标准库中的copy模块。
#
# 1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。
# 2. copy.deepcopy 深拷贝 拷贝对象及其子对象

listSix = [1, 2, 3]
listSeven = listSix
listSix.reverse()

print(listSeven)


# 编写一个程序，求 100~999 之间的所有水仙花数。
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。

for idx in range(100, 1000):
    if idx == sum(list(map(lambda x: int(x) ** 3, list(str(idx))))):
        print(idx)
