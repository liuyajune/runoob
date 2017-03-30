#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
说明：python2.7的 /  与  Python3.5 的 / 不一样 ,对于 // 没有区别
python2.7   987/10=98  987//10=98
python3.5  987/10=98.7  998//10=98
'''
import math
for num in range(100, 999):
    #个位
    i = num % 10
    #十位
    j = num // 10 % 10
    #百位
    k = num // 100

    if num == math.pow(i, 3) + math.pow(j, 3) + math.pow(j, 3):
        print(num)