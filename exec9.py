#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：暂停一秒输出。

程序分析：无。
注意：dict1的值输出并不按顺序
'''
import time
dict1 = {'a':'hello', 'b':'world', 'c':'test'}
for  key, value in dict1.items():
    print('key:', key , 'value:', value)
    time.sleep(2)


for key in dict1.keys():
    print(key)
    