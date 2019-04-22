#!/usr/local/bin/python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 AM10:30
# @Author  : L
# @Email   : L862608263@163.com
# @File    : l_log.py
# @Software: PyCharm

import sys
from datetime import *


# typedef struct _frame {
#     PyObject_VAR_HEAD
#     struct _frame *f_back;    /* 调用者的帧 */
#     PyCodeObject *f_code;     /* 帧对应的字节码对象 */
#     PyObject *f_builtins;     /* 内置名字空间 */
#     PyObject *f_globals;      /* 全局名字空间 */
#     PyObject *f_locals;       /* 本地名字空间 */
#     PyObject **f_valuestack;  /* 运行时栈底 */
#     PyObject **f_stacktop;    /* 运行时栈顶 */
#     …….
# }

# 单星号传入元组
# 双星号传入map
# *args 和**kwargs
def l_log(*args):
    frame = sys._getframe()

    now_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # frame.f_back.f_code.co_filename 全部路径
    # str(frame.f_back.f_code.co_filename).split("/")[-1] 只要文件名
    file_path = str(frame.f_back.f_code.co_filename).split("/")[-1]

    func = frame.f_back.f_code.co_name

    line = frame.f_back.f_lineno

    if len(args) == 1:
        output = args[0]
    else:
        output = args

    print('\n[time:%s] [file:%s] [func:%s] [line:%s] \n[content: %s]' % (now_time, file_path, func, line, output))
