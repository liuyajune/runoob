#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

程序分析：无。

重点：文件打开方式   r , w，x, a,b,t ,+,U (注意：没有rw)     file对象可迭代  for in
File对象方法
OS对象方法

'''

import os

with open('test1.txt') as f1:
    line1 = f1.read()
#    print(line1)
with open('test2.txt') as f2:
    line2 = f2.read()
#    print(line2)
words = line1 + line2
#print(words)

with open('test3.txt','w') as f3:
    f3.write(words)