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
