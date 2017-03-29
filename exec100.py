#/usr/bin/env python
#-*- coding:utf-8 -*-

'''
题目：列表转换为字典。

程序分析：无。
zip()的使用方法
map()使用方法
lambda使用方法
'''

list1 = [1,2,3,4]
list2 = ['a','b','c','d']
dict1 = dict(zip(list1,list2))
#dict1 = dict(list1)
dict2 = dict(map(lambda x,y:[x,y], list1,list2))
#print(dict1)
print(dict2)
