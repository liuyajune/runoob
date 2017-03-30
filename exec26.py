#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!
'''
def  fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

print(fac(5))