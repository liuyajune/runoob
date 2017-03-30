#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
else语句中不能有其他的条件语句  ，如： else score < 60:语法错误
提示；可否使用三元表达式实现？
'''

score = 95
if score > 90:
    print('A')
elif 60<= score <= 80:
    print('B')
else:
    print('C')


#使用三元表达式
result = 'A' if score > 90 else ('B' if 60 <=score <= 80 else 'C')
print(result)