#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 PM10:46
# @Author  : L
# @Email   : L862608263@163.com
# @File    : process.py
# @Software: PyCharm


# 要让Python程序实现多进程(multiprocessing),我们先了解操作系统的相关知识.
#
# Unix / Linux操作系统提供了一个fork()系统调用, 它非常特殊.
#
# 普通的函数调用,调用一次,返回一次. 但是fork()调用一次,返回两次.
#
# 因为操作系统自动把当前进程 (称为父进程) 复制了一份 (称为子进程), 然后, 分别在父进程和子进程内返回.
#
# 子进程永远返回0, 而父进程返回子进程的ID。
#
# 这样做的理由是, 一个父进程可以fork出很多子进程.
#
# 所以,父进程要记下每个子进程的ID, 而子进程只需要调用getppid()就可以拿到父进程的ID。


# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程:

import os
import time
import random
from multiprocessing import Process, Pool


# 终端top命令查看

# while 1:
#     print('Process(python3.6) %s start... Father Process(pycharm) is %s' % (os.getpid(), os.getppid()))

# Only works on Unix/Linux/Mac:
def create_child_process():
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.\n' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# create_child_process()


# NOTE multiprocessing

# 由于Windows没有fork调用 Python是跨平台的，自然也应该提供一个跨平台的多进程支持。
# multiprocessing模块就是跨平台版本的多进程模块。

# multiprocessing模块提供了一个Process类来代表一个进程对象.

# NOTE Process 类的构造方法
# def __init__(self, group=None, target=None, name=None, args=(), kwargs={})

# group：进程所属组
# target：进程调用对象（可以是一个函数名，也可以是一个可调用的对象（实现了__call__方法的类））
# name：进程别名 (通过p.name查看)
# args：调用对象的位置参数元组
# kwargs：调用对象的关键字参数字典

# NOTE Process 类的实例方法

# is_alive()：返回进程是否在运行
# start()：启动进程，等待CPU调度
# join([timeout])：阻塞当前上下文环境，直到调用此方法的进程终止或者到达指定timeout
# terminate()：不管任务是否完成，立即停止该进程
# run()：start()调用该方法，当实例进程没有传入target参数，stat()将执行默认的run()方法

# NOTE 属性
# name：进程名
# daemon：进程的守护程序标志, 一个布尔值。这必须在调用 start() 之前设置。
# authkey：进程的身份验证密钥
# exitcode：进程的退出状态码
# ident: 进程的返回标识符（PID）或者如果尚未启动则返回“None”
# pid：返回进程id
# sentinel: 返回适合等待进程终止的文件描述符（Unix）或句柄（Windows）。


# 下面的例子演示了启动一个子进程并等待其结束:

# 子进程要执行的代码
def run_process(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def process_demo():
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
    # 这里的test, 是run_process方法的传入参数
    p = Process(target=run_process, name="demo_process", args=("test",))
    print('Child process will start.')
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print(p.name)
    print('Child process end.')


# process_demo()

# NOTE Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def pool_demo():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for idx in range(5):
        p.apply_async(long_time_task, args=(idx,))
    print('Waiting for all sub processes done...')
    p.close()
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.join()
    print('All sub processes done.')


# task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行.
# 这是因为 Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。 这是Pool有意设计的限制，并不是操作系统的限制。 如果改成：
# p = Pool(5)
# 就可以同时跑5个进程。
# 由于Pool的默认大小是CPU的核数，如果你拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

# pool_demo()

# NOTE 子进程

import subprocess

# 调用子进程的推荐方法是对它可以处理的所有用例使用 run() 函数。对于更高级的用例, 可以直接使用底层的 Popen 接口。
# subprocess.(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None,
#              timeout=None, check=False, encoding=None, errors=None, text=None, env=None)

# 运行args描述的命令。 等待命令完成，然后返回CompletedProcess实例。
# 上面显示的参数仅仅是最常见的参数，在下面的常用参数中进行了描述（因此在缩写签名中使用了仅关键字符号）。
# 完整的函数签名与Popen构造函数的签名大致相同 - 此函数的大多数参数都传递给该接口。 （超时，输入，检查和capture_output不是。）

# 如果capture_output为true，则将捕获stdout和stderr。
# 使用时，将使用stdout = PIPE和stderr = PIPE自动创建内部Popen对象。 也可能不使用stdout和stderr参数。

# timeout参数传递给Popen.communicate（）。 如果超时到期，子进程将被终止并等待。 子进程终止后，将重新引发TimeoutExpired异常。

# 输入参数传递给Popen.communicate（），从而传递给子进程的stdin。
# 如果使用它必须是字节序列，或者如果指定了编码或错误或文本为真，则必须是字符串。
# 使用时，使用stdin = PIPE自动创建内部Popen对象，也可以不使用stdin参数。

# 如果check为true，并且进程以非零退出代码退出，则将引发CalledProcessError异常。
# 该异常的属性包含参数，退出代码以及stdout和stderr（如果它们被捕获）。

# 如果指定了编码或错误，或者text为true，则使用指定的编码和错误或io.TextIOWrapper默认值在文本模式下打开stdin，stdout和stderr的文件对象。
# universal_newlines参数等同于text，用于向后兼容。 默认情况下，文件对象以二进制模式打开。

# 如果environment不是None，则它必须是定义新进程的环境变量的映射; 这些是用来代替继承当前进程环境的默认行为。 它直接传递给Popen。

# demo

# 不捕获输出
subprocess.run("ping baidu.com -c 3", shell=True)

# 相当于
subprocess.CompletedProcess(args="ping baidu.com -c 3", returncode=0)
