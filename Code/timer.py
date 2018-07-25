#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 PM11:01
# @Author  : L
# @Email   : L862608263@163.com
# @File    : timer.py
# @Software: PyCharm

import threading
import time


class BaseTimer(threading.Thread):  # from abc import ABCMeta, abstractmethod , metaclass=ABCMeta
    """
    基础定时器抽象类，可以随意继承本类并且实现exec抽象方法即可定时产生任务
    """

    def __init__(self, task=None, time_interval=1.0, repeats=True, enable_log=False):
        """
        task 定时任务
        time_interval 每次执行间隔的时间
        repeats 是否重复执行定时任务
        enable_log 是否开启log
        """

        self.repeats = repeats

        self.time_interval = time_interval

        self.enable_log = enable_log

        self.task = task

        threading.Thread.__init__(self)

        if enable_log:
            print("Timer initialized")

    def run(self):
        """
        开启定时器
        """
        if self.enable_log:
            print("Timer running")

        self.exec()

        while self.repeats:
            time.sleep(self.time_interval)

            self.exec()

    # @abstractmethod
    # 使用abstractmethod修饰符, 并在继承的位置,设定metaclass=ABCMeta, 导入ABCMeta, abstractmethod模块

    # (以上实现方式,在Python不通版本中,稍有不同  这里只是按照当前的Python版本做个demo)

    # 可以使子类必须实现exec方法, 否则报错
    # TypeError: Can't instantiate abstract class BaseTimer with abstract methods exec

    # 但是这样的话, 基类直接初始化定时执行方法的流程就走不通了(demo_two), 所以这里先不用

    def exec(self):
        """
        抽象方法，子类实现
        实现具体的定时任务
        """
        if self.task is not None:
            self.task()
        if self.enable_log:
            print("Timer exec")
        pass

    def destroy(self):
        """
        销毁自身
        """
        self.repeats = False
        if self.enable_log:
            print("Timer destroy")
        del self

    def stop(self):
        """
        暂停定时器
        """
        self.repeats = False
        if self.enable_log:
            print("Timer stop")

    def restart(self):
        """
        重启定时器
        """
        self.repeats = True
        if self.enable_log:
            print("Timer restart")

    def get_status(self):
        """
        获取定时器状态
        """
        return self.repeats


class Heartbeat(BaseTimer):
    """
    定时任务类，不同的业务逻辑
    """

    def __init__(self, task=None, time_interval=1.0, repeats=True, enable_log=False):
        BaseTimer.__init__(self, task, time_interval, repeats, enable_log)
        self.counter = 0

    def exec(self):
        super().exec()  # 执行父类方法
        print("Alive !!!!")
        self.counter += 1
        if self.counter > 5:
            self.destroy()


def demo_one():
    heart_beat = Heartbeat(time_interval=5, enable_log=True)
    heart_beat.run()


def demo_two():
    timer = BaseTimer(task=demo_two_task)  # , enable_log=True
    timer.run()


def demo_two_task():
    print("task running")


if __name__ == "__main__":
    # demo_one()
    demo_two()
