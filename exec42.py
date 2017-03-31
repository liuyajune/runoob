#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：学习使用auto定义变量的用法。

程序分析：没有auto关键字，使用变量作用域来举例吧。
知识点：命名空间的使用方法
'''
num = 2
def autofunc():
    num = 1
    print('internal block num = %d' % num)
    num += 1
for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()