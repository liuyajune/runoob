#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：时间函数举例1。

程序分析：无。
'''
import time
if __name__ == '__main__':
    print(time.time())
    print(time.ctime())
    print(time.asctime(time.localtime()))