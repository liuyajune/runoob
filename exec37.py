#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：对10个数进行排序。

程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，s
即用第二个元素与后8个进行比较，并进行交换。
选择排序
'''

N = 10
# input data
l = [11, 12, 8, 9, 10, 7, 15, 18, 5, 19]
print(l)
# sort ten num
for i in range(N - 1):
    min = i
    for j in range(i + 1, N):
        if l[min] > l[j]:
            min = j
    l[i],l[min] = l[min],l[i]
print('after sorted')
for i in range(N):
    print(l[i], end=' ')