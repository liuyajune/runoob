#/usr/bin/env python
#-*- coding:utf-8 -*-

'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

程序分析：无。
'''
# i = 0
# while i < 7:
#     number = int(input('input number：'))
#     print('*' * number)
#     i += 1


for i in range(7):
    number = int(input('input number：'))
    print('*' * number)