#! /usr/bin/env  python
#-*- coding:utf-8 -*-
'''题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
重点: print()关于字符串格式化显示
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            #print('number %d%d%d'% (i,j,k))
            if (i != j) and (i != k) and (j != k):
                print("number {i}{j}{k}".format(i=i,j=j,k=k))