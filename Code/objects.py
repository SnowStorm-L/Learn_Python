#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 PM2:29
# @Author  : L
# @Email   : L862608263@163.com
# @File    : objects.py
# @Software: PyCharm


import random

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
# 如果子类中定义与父类相同的方法或属性,则会自动覆盖父类对应的方法属性
#     子类      (基类、父类或超类)
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
# 把双__的私有变量自动改了名  改成(_类名__变量名)(_类名__方法名())
# python 的私有机制,是伪私有
# print(ball._Ball__private_property)

# 公有和私有

# 默认的函数变量都是公有的

# 在py中定义私有变量只需在变量或函数名前面加"__"两个下划线,那么这个函数或变量就会成为私有的了


# demo

class Fish:

    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        self.x -= 1
        print('location: ', self.x, self.y)


class GoldFish(Fish):
    pass


class Carp(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):

    def __init__(self):
        # 这里重写了父类的init方法,会导致没有x属性
        # 解决方法有2种
        # 1, 调用未绑定的父类方法
        #    Fish.__init__(self)  # Fish.__init__(调用父类的方法),这个self是Shark(子类的实例对象)
        # 2, 使用super函数
        super().__init__()
        self.hungry = True

    def eat(self):
        print("好吃" if self.hungry else "吃太多了")
        self.hungry = not self.hungry


fish = Fish()
fish.move()

gold_fish = GoldFish()
gold_fish.move()

shark = Shark()
# 调用未绑定的父类方法相当于进行了以下操作
# Fish.__init__(shark)
shark.move()


# python 支持多重继承


class BaseClassOne:

    # noinspection PyMethodMayBeStatic
    def say_one(self):
        print('i`m BaseClassOne')


class BaseClassTwo:

    # noinspection PyMethodMayBeStatic
    def say_two(self):
        print('i`m BaseClassTwo')


# 多继承实现
class SomeClass(BaseClassOne, BaseClassTwo):
    pass


some_class = SomeClass()
some_class.say_one()
some_class.say_two()
# mro查看继承关系
print(SomeClass.__mro__)

# Mixin 编程是一种开发模式，是一种将多个类中的功能单元的进行组合的利用的方式，
# 这听起来就像是有类的继承机制就可以实现，然而这与传统的类继承有所不同。
# 通常 Mixin 并不作为任何类的基类，也不关心与什么类一起使用，而是在运行时动态的同其他零散的类一起组合使用

# 使用 Mixin 机制有如下好处：
# 可以在不修改任何源代码的情况下，对已有类进行扩展；
# 可以保证组件的划分；
# 可以根据需要，使用已有的功能进行组合，来实现“新”类；
# 很好的避免了类继承的局限性，因为新的业务需要可能就需要创建新的子类。

# 插件方式

# 以上方式，都是基于多继承和python的元编程特性，然而在业务需求变化时，就需要新的功能组合，
# 那么就需要重新修改A的基类，这回带来同步的问题，因为我们改的是类的特性，而不是对象的。
# 因此以上修改会对所有引用该类的模块都收到影响，这是相当危险的。
# 通常我们希望修改对象的行为，而不是修改类的。同样的我们可以利用__dict__来扩展对象的方法。


class PlugIn(object):
    """object 是大多数类的基类, 可以省略 """
    def __init__(self):
        self._exported_methods = []
  
    def plug_in(self, owner):
        for f in self._exported_methods:
            owner.__dict__[f.__name__] = f

    def plug_out(self, owner):
        for f in self._exported_methods:
            del owner.__dict__[f.__name__]


class AFeature(PlugIn):

    def __init__(self):
        super().__init__()
        self._exported_methods.append(self.get_a_value)

    # noinspection PyMethodMayBeStatic
    def get_a_value(self):
        print('a feature.')


class BFeature(PlugIn):

    def __init__(self):
        super(BFeature, self).__init__()
        self._exported_methods.append(self.get_b_value)

    # noinspection PyMethodMayBeStatic
    def get_b_value(self):
        print('b feature.')


class Combine:
    pass


c = Combine()

AFeature().plug_in(c)
BFeature().plug_in(c)

c.get_a_value()
c.get_b_value()


# 类和对象相关的BIF

# issubclass(class, classinfo)
# 第一个class是第二个classinfo的子类,就返回true

# 非严格性检查
# 1,一个类被认为是其自身的子类
# 2,classinfo可以是类对象组成的元组, 只要class与其中任何一个候选类的子类,则返回true

# 检查实例对象是否属于一个类(classinfo)的
# isinstance(object, classinfo)

# 非严格性检查
# 1,如果第一个参数不是对象,则永远返回False
# 2,如果第二个参数不是类或者由类对象组成的元祖,会抛出一个TypeError异常
# 3,classinfo可以是类对象组成的元组, 只要class与其中任何一个候选类的子类,则返回true

# attribute: 属性
# 检查对象是否有指定属性
# name要用字符串
# hasattr(object, name)

# 返回对象指定的属性值
# 如果指定属性不存在,并且设置了default,就会把default打印出来
# 否则抛出AttributeError的异常
# getattr(object, name, default=None)

# 设置对象属性值,如果不存在,会新创建
# setattr(object, name, value)

# 删除对象指定的属性
# delattr(object, name)

# 通过属性设置属性
# 用途--设置对外接口(可以不用经常改变), 对内的只是方法(用户只调x操作)
# property(fget=None, fset=None, fdel=None, doc=None)


# class Demo:
#
#     def __init__(self, value=10):
#         self.size = value
#
#     def get_size(self):
#         return self.size
#
#     def set_size(self, value):
#         self.size = value
#
#     def del_size(self):
#         del self.size
#
#     x = property(get_size, set_size, del_size)
#
#
# demo = Demo()
# demo.x = 20
