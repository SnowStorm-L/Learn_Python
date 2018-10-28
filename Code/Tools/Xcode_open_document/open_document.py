#!/usr/local/bin/python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 PM11:22
# @Author  : L
# @Email   : L862608263@163.com
# @File    : open_document.py
# @Software: PyCharm

import os.path

# Xcode 的 shell 里面添加py的路径(这个路径,修改为.py上层文件夹的路径)(自己工程)
# cd ${SRCROOT}/${TARGET_NAME}/Tools/OpenDocumentPython


# 项目的bundle id 加.plist
bundle_id = 'com.bestidear.A113D.plist'


# 自己电脑的根文件夹路径
def get_document(at_path='/Users/l/Library/Developer/CoreSimulator/Devices/'):
    files = os.listdir(at_path)
    for fi in files:
        fi_d = os.path.join(at_path, fi)
        if os.path.isdir(fi_d):
            get_document(fi_d)
        else:
            if fi_d.split('/')[-1] == bundle_id:
                result = '/'.join(os.path.join(at_path, fi_d).split('/')[:-3])
                command = "open %s" % result
                os.system(command)
