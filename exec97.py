#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：从键盘输入一些字符，逐个把它们送到磁盘上去，直到输入一个#为止。

程序分析：无。
重点： while 循环使用， 标准输入输:  stdin，stdout
sys模块的使用
stdout.write 输出到屏幕
'''

from sys import  stdout
#fileName = input('input filename:')
with open('test97.txt', 'w') as f1:
    ch = input("input char")
    while (ch != '#'):
        f1.write(ch)
        stdout.write(ch)
        ch = input('')