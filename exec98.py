#/usr/bin/env python
#-*- coding:utf-8 -*-

'''
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

程序分析：无。
重点：字符串函数   join ,split  ，upper ,lower , isXXX
'''
import string
str1 = input('input a string:')
str2 = str1.upper()
with open('exc98.txt','w') as  f1:
    f1.write(str2)
    print(str2)