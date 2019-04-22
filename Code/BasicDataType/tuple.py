# 元组
# 元组的关键标志不是(), 是逗号
newTuple = (1, 2, 3, 4, 5)

print(newTuple[1])

print(newTuple[3:])

print(newTuple[:2])

# 元组不能被修改
# newTuple[1] = 3
# TypeError: 'tuple' object does not support item assignment

testTupleOne = (1)
# 输出 <class 'int'>
print(type(testTupleOne))

testTupleTwo = 1, 2, 3, 4
# 输出 <class 'tuple'>
print(type(testTupleTwo))

# 空元组创建
emptyTuple = ()

# 单数据元组
# tupleNew = 1,
# tupleNew = (1,)

# (8, 8, 8, 8, 8, 8, 8, 8)
# print(8 * (8, ))
# 乘号是重复操作符

tupleOperational = ('一', '二', '三')

# 加入
tupleOperational = tupleOperational[:2] + ('新的',) + tupleOperational[2:]

print(tupleOperational)

# 删除
# del整个删除或者用[:]切片
del tupleOperational
