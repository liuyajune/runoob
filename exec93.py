#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：时间函数举例3。

程序分析：无。

'''
import  time
start =  time.clock()
for i in range(1000):
    print(i)
end = time.clock()
print('diffent is %.5f' % (end - start))
