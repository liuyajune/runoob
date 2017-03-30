#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：求一个3*3矩阵对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
map()
reduce()
zip()
'''
from functools import reduce
matrix1 = []
for i in range(3):
    matrix1.append([])
    for j in range(3):
        matrix1[i].append(float(input("input num:\n")))

print(matrix1)
sum = 0
for arr1 in matrix1:
    for item1 in arr1:
        sum += int(item1)
print(sum)

#reduce，map，filter函数第二个参数要求是可迭代对象
sum1 = 0
for arr2 in matrix1:
        sum1 += reduce(lambda x, y: x + y, arr2)
print(sum1)
