#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
psr-4  php代码编写规范
pep8  python代码编写规范
'''
for i  in range(1, 10):
    print()
    for j in range(1, 10):
        if i <= j:
            print("%d * %d = %d "% (i, j, i * j), end=" ")