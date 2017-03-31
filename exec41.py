#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：模仿静态变量的用法。

程序分析：无。
知识点：
    静态变量， 类属性， 对象属性
'''
def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1

if __name__ == '__main__':
    for i in range(3):
        varfunc()


class StaticVar:
    sVar =  5
    def varfunc(self):
        self.sVar += 1
        print('var = %d' % self.sVar)

print(StaticVar.sVar)

s = StaticVar()
for i in range(3):
    s.varfunc()