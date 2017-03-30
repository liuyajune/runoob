#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用while语句,条件为输入的字符不为'\n'。
'''
import string
str1 = input('input a string')
letter = 0
space = 0
digit = 0
other = 0

for ch in str1:
    if ch.isalpha():
        letter += 1
    elif ch.isspace():
        space += 1
    elif ch.isdigit():
        digit += 1
    else:
        other += 1
print('char = %d,space = %d,digit = %d,other = %d' % (letter, space, digit, other))