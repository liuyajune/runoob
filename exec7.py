#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。
列表切片
深拷贝
列表推导式
'''
list1 = [1, 2, 3, 4]

import copy
list2 =  copy.deepcopy(list1)
list3 = list1[::1]
list4 = [var for var in list1]
print(list2)
print(list3)
print(list4)