#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
序列排序：
冒泡，选择，插入，归并，快速，桶排序，堆排序
'''
list1 = [1, 2, 3, 5, 7]
num = int(input('input a num:'))
list1.append(num)
for i in range(len(list1)):
    if num > list1[i]:
        pass


print(list1)