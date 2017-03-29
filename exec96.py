#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：计算字符串中子串出现的次数。

程序分析：无。
count , 统计每个单词出现的频率
使用set
扩展：使用set实现统计某个单词出现的频率

'''

str1 = input('input a string:\n')
str2 = input('input a sub string:\n')
ncount = str1.count(str2)
print(ncount)

'''
    str1 = input('input a string')
    list1 = str1.split()
    list2 = [word.strip(',') for word in list1]
    set2 = set(list2)
    dict1 = {}
    for w in set2:
	dict1[w]= str1.count(w)
'''
