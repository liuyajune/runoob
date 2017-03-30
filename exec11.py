#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
'''

def fib(n):
    if n == 0:
        return  1
    if n == 1:
        return  1
    return fib(n - 1) + fib(n  - 2)

print(fib(5))

sum  = 0
for i in range(5):
    sum += fib(i)
print(sum)

#
# 使用类方式定义fib，使用方法和属性
#
class  Fib:
    def __init__(self,n):
        self.n = n
        self.sum = 0

    def __fib(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.__fib(n - 1) + self.__fib(n - 2)

    def count(self):
        for i in range(self.n):
            self.sum += self.__fib(i)
            print('%d month %d rabbit' % (i, self.__fib(i)))
        print("total rabbit is %d" % self.sum)

f = Fib(5)
f.count()


f1 = 1
f2 = 1
for i in range(1,22):
    print('%12ld %12ld' % (f1, f2),)
    if (i % 3) == 0:
        print()
    f1 = f1 + f2
    f2 = f1 + f2