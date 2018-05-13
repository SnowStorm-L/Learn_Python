#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 PM2:29
# @Author  : L
# @Email   : L862608263@163.com
# @File    : objects.py
# @Software: PyCharm

# 对象 = 属性 + 方法


# 类

class Turtle:  # Py 中的类名约定以大写字母开头

    """关于类的一个简单例子"""
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法

    def run(self):
        print('乌龟用{0}条腿跑'.format(self.legs))


# 继承  ()里面写父类
class SonTurtle(Turtle):
    pass  # pass 代表不做任何事情


# 多态
class BigTurtle(Turtle):

    def run(self):
        print('大乌龟用{0}条腿跑'.format(self.legs))


class SmallTurtle(Turtle):

    def run(self):
        print('小龟用{0}条腿跑'.format(self.legs))


# 生成类的实例对象
turtle = Turtle()
turtle.run()

SonTurtle().run()

# oop  python也是oop(面向对象)编程

# oop的3大特点 继承,封装,多肽

# 多态就是多种形态。
# 继承了就有多态了。
# 继承了就具有父类的方法，然后子类就能够覆写父类方法，子类就能够调用该方法实现自己的需求。
# 这样的好处就是，一个方法名在不同的子类里具有不同的作用。

small_turtle = SmallTurtle()
big_turtle = BigTurtle()

# small_turtle 不仅是Turtle还是SmallTurtle
print(isinstance(small_turtle, SmallTurtle))
print(isinstance(small_turtle, Turtle))

# python 的self相当于cplusplus的this指针


class Ball:

    input_name = ''

    __private_property = "私有属性"

    # 重写私有属性的get方法,供外部使用
    def get_private_property(self):
        return self.__private_property

    # 重写实例化方法
    def __init__(self, name):
        self.input_name = name

    def set_name(self, name):
        self.input_name = name

    def kick(self):
        print('%s踢了我' % self.input_name)


# ball = Ball()
# print(ball.input_name)
ball = Ball('波波')
# ball.set_name('保龄球')
# kick这里有第一个隐藏参数,self
ball.kick()

# name mangling (名字改编,名字重整) 私有属性的内部实现
print(ball.get_private_property())
# 把双__的私有变量自动改了名  改成(_类名__变量名)
# python 的私有机制,是伪私有
print(ball._Ball__private_property)

# 公有和私有

# 默认的函数变量都是公有的

# 在py中定义私有变量只需在变量或函数名前面加"__"两个下划线,那么这个函数或变量就会成为私有的了
