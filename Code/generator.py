#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 AM10:22
# @Author  : L
# @Email   : L862608263@163.com
# @File    : generator.py
# @Software: PyCharm

# 生成器的发明使python模仿协同程序的方法得以实现
# 所谓的协同程序就是可以运行独立函数调用,函数可以暂时或者挂起,并在需要的时候从程序离开的地方继续或者重新开始


def my_generator():
    print('生成器被执行 !')
    yield 1
    yield 2


demo = my_generator()
print(next(demo))
print(next(demo))


# next(demo) StopIteration


# 斐波那契数列
def fib(limit=10):
    a, b = 0, 1
    for _ in range(limit):
        yield b
        a, b = b, a + b


for each in fib():
    print(each, end=" ")
print("\n")

# NOTE yield 关键字的理解

# 为了理解什么是 yield,你必须理解什么是生成器。
# 在理解生成器之前，让我们先走近迭代。

# NOTE 可迭代对象(Iterables)

# 当你建立了一个列表，你可以逐项地读取这个列表，这叫做一个可迭代对象:
my_list = [1, 2, 3]
for i in my_list:
    print(i)

# my_list 是一个可迭代的对象。

# 当你使用一个列表推导式来建立一个列表的时候，就建立了一个可迭代的对象:
other_list = [x * x for x in range(3)]
for i in other_list:
    print('列表推导式', i)

# other_list 也是一个可迭代的对象。

# NOTE 所有你可以使用 for .. in .. 语法的叫做一个迭代器：列表，字符串，文件....
# 你经常使用它们是因为你可以如你所愿的读取其中的元素，但是你把所有的值都存储到了内存中，如果你有大量数据的话这个方式并不是你想要的。

# NOTE 生成器(Generators)
# 生成器是可以迭代的，但是你 只可以读取它***一次***, 因为它并不把所有的值放在内存中，它是实时地生成数据(会动态生成值):
# 这一方面, 有点类似于懒加载
my_generator = (x * x for x in range(3))
for i in my_generator:
    print('第一次读取', i)

# 看起来除了把 [] 换成 () 外没什么不同。
# 但是，你不可以再次使用 for i in my_generator , 因为生成器只能被迭代一次：
# 先计算出0，然后继续计算1 ，然后计算4，一个跟一个的...
for i in my_generator:
    print('第二次读取', i)


# NOTE yield关键字
# NOTE yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。

def create_generator():
    print("这个地方执行了")
    my_range = range(3)
    for idx in my_range:
        print("第 %d 次 yeild" % idx)
        yield idx * idx


demo = create_generator()  # create a generator
print(demo)  # demo is an object!

# for之前create_generator是没有执行的, 如果没有yield 关键字就执行了
for i in demo:
    print(i)


# 这个例子没什么用途，但是它让你知道，这个函数会返回一大批你只需要读一次的值.

# 为了精通 yield ,你必须要理解：

# 当你调用这个函数的时候，函数内部的代码***并不立马执行***(不使用for之前,看print有没有打印)
# 这个函数只是返回一个生成器对象，这有点蹊跷不是吗。

# 那么，函数内的代码什么时候执行呢？ 当你使用for进行迭代的时候.

# NOTE 现在到了关键点了！

# NOTE 第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值(idx * idx), 作为第一次迭代的返回值.

# NOTE 然后，每次执行这个函数, 都会继续执行你在函数内部定义的那个循环(for idx in my_range:)的下一次，再返回那个值，直到没有可以返回的。

# NOTE 如果生成器内部没有定义 yield 关键字，那么这个生成器被认为成空的。 这可能是因为循环已经结束, 或者因为您不再满足"if/else"了。


# NOTE yield from 关键字

# 官方解释：
#
# Python3.3版本的PEP 380中添加了yield from语法，允许一个generator生成器将其部分操作委派给另一个生成器。

# 其产生的主要动力在于使生成器能够很容易分为多个拥有send和throw方法的子生成器，像一个大函数可以分为多个子函数一样简单。

# Python的生成器是协程coroutine的一种形式，但它的局限性在于只能向它的直接调用者yield值。

# 这意味着那些包含yield的代码不能想其他代码那样被分离出来放到一个单独的函数中。 这也正是yield from要解决的。

# 虽然yield from主要设计用来向子生成器委派操作任务，但yield from可以向任意的迭代器委派操作；

# NOTE 下面分3个demo 来讲解yield from 的使用场景

# 1. 利用yield from从生成器读取数据
# 对于简单的迭代器，yield from iterable本质上等于for item in iterable: yield item的缩写版，如下所示：

def yield_from(x):
    yield from range(x, 0, -1)
    yield from range(x)


def yield_demo(y):
    for idx in range(y, 0, -1):
        yield idx
    for idx in range(y):
        yield idx


# 以上2种写法是一样的
print(list(yield_from(5)))
print(list(yield_demo(5)))


# 2.利用yield from语句向生成器（协程）传送数据
# 然而，不同于普通的循环，yield from允许子生成器直接从调用者接收其发送的信息或者抛出调用时遇到的异常，并且返回给委派生产器一个值，如下所示：


def accumulate():  # 子生成器，将传进的非None值累加，传进的值若为None，则返回累加结果
    tally = 0
    while 1:
        temp = yield
        if temp is None:
            return tally
        tally += temp


def gather_tallies(array):  # 外部生成器，将累加操作任务委托给子生成器
    while 1:
        tally = yield from accumulate()
        array.append(tally)


tallies = []
acc = gather_tallies(tallies)
next(acc)  # 使累加生成器准备好接收传入值

for i in range(4):
    acc.send(i)

acc.send(None)  # 结束第一次累加

for i in range(5):
    acc.send(i)

acc.send(None)  # 结束第二次累加
print(tallies)  # 输出最终结果[6, 10]


# 3. 利用yield from向生成器传送数据–处理异常


class SpamException(Exception):
    pass


def writer_wrapper(coro):
    """手动捕获异常并抛出异常"""
    # coro.send(None)  # prime the coro
    # while True:
    #     try:
    #         try:
    #             x = (yield)
    #         except Exception as e:  # This catches the SpamException
    #             coro.throw(e)
    #         else:
    #             coro.send(x)
    #     except StopIteration:
    #         pass

    # 以上代码可以使用以下代码一句替代(效果是一样的)
    yield from coro


def writer():
    while True:
        try:
            temp = (yield)
        except SpamException:
            print('***')
        else:
            print('>> ', temp)


w = writer()
wrap = writer_wrapper(w)
wrap.send(None)  # ***协程
for i in [0, 1, 2, 'spam', 4]:
    if isinstance(i, str):
        wrap.throw(SpamException)
    else:
        wrap.send(i)
