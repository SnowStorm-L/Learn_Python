#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 PM5:31
# @Author  : L
# @Email   : L862608263@163.com
# @File    : set.py
# @Software: PyCharm


# 集合是无序,唯一的
# {}之内没有固定的对应关系,就会被认为是集合(set)

normalset = {1, 1, 2, 3, 4}
listset = set(list([1, 2, 3, 4]))

print(type(normalset))
print(normalset)
print(listset)

# for in 把集合元素读取出来

for each_value in normalset:
    print(each_value)

# in, not in 判断元素是否在集合内

print(5 in normalset)
print(5 not in normalset)

# add, remove  添加/移除 集合中的元素
normalset.add(5)
normalset.remove(1)

print(normalset)

# 不可变集合
immutableset = frozenset([1, 1, 2, 3])

print(immutableset)

# 集合bif

# 集合（s）.方法名                   等价符号                        方法说明
# s.issubset(t)                    s <= t                   子集测试（允许不严格意义上的子集）：s中所有的元素都是t的成员
#                                  s < t                    子集测试（严格意义上）：s != t而且s中所有的元素都是t的成员
# s.issuperset(t)                  s >= t                   超集测试（允许不严格意义上的超集）：t中所有的元素都是s的成员
#                                  s > t                    超集测试（严格意义上）：s != t而且t中所有的元素都是s的成员
# s.union(t)                       s | t                    合并操作：s"或"t中的元素
# s.intersection(t)                s & t                    交集操作：s"与"t中的元素
# s.difference                     s - t                    差分操作：在s中存在，在t中不存在的元素
# s.symmetric_difference(t)        s ^ t                    对称差分操作：s"或"t中的元素，但不是s和t共有的元素
# s.copy()                                                  返回s的拷贝（浅复制）
#
# 以下方法仅适用于可变集合
# s.update                        s |= t                    将t中的元素添加到s中
# s.intersection_update(t)        s &= t                    交集修改操作：s中仅包括s和t中共有的成员
# s.difference_update(t)          s -= t                    差修改操作：s中包括仅属于s但不属于t的成员
# s.symmetric_difference_update(t)s ^= t                    对称差分修改操作：s中包括仅属于s或仅属于t的成员
# s.add(obj)                                                加操作：将obj添加到s
# s.remove(obj)                                             删除操作：将obj从s中删除，如果s中不存在obj，将引发异常
# s.discard(obj)                                            丢弃操作：将obj从s中删除，如果s中不存在obj，也没事儿 ^ _ ^
# s.pop()                                                   弹出操作：移除并返回s中的任意一个元素
# s.clear()                                                 清除操作：清除s中的所有元素
