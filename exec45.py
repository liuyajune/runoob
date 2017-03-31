#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：统计 1 到 100 之和。

程序分析：无
lambda使用方式：
 lambda x, y: x + y
 reduce(lambda x, y: x + y, range(1, 101))
 map(lambda x: x + 2, range(1, 101))
'''
from functools import reduce
tmp = 0
for i in range(1,101):
    tmp += i
print('The sum is %d' % tmp)

sum = reduce(lambda x,y :x + y, range(1, 101))