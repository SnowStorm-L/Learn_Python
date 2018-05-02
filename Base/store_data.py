#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 PM4:39
# @Author  : L
# @Email   : L862608263@163.com
# @File    : store_data.py
# @Software: PyCharm

# 存储

import pickle

# 天气查询 import
import urllib.request
import json

# store_list = [123, '456', ('123', 213)]
#
# # wb  write Binary 二进制写入
# pickle_file = open('/Users/l/Desktop/store_list.pickle', 'wb')
#
# # 存储
# pickle.dump(store_list, pickle_file)
#
# pickle_file.close()
#
# # rb read Binary 二进制读取
# pickle_file = open('/Users/l/Desktop/store_list.pickle', 'rb')
#
# read_list = pickle.load(pickle_file)
#
# print(read_list)

# 天气查询

pickle_file = open('../Resource/city_data.pkl', 'rb')
city = pickle.load(pickle_file)
city_name = input('请输入城市:')
city_id = city[city_name]
url = 'https://link.jianshu.com/?t=http://www.weather.com.cn/data/sk/'+city_id+'.html'
print(url)
file = urllib.request.urlopen(url)  # 打开url
weather_HTML = file.read().decode('utf-8')  # 读入打开的url
weather_JSON = json.JSONDecoder().decode(weather_HTML)  # 创建json
weather_Info = weather_JSON['weatherinfo']
print(weather_Info)

# 打印信息
print('城市：', weather_Info['city'])
print('时间：', weather_Info['time'])

input('按任意键退出：')
