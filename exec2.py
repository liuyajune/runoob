#/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%；
    高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
重点：if 语句, python模拟switch ,case语句的使用技巧
'''

#profite = int(input('输入利润：(万元)'))

# if (profite>100):
#     rate =  100 * 0.1 + (profite - 100) * 0.01
# elif(100 >= profite > 60):
#     rate = 60 * 0.1 + (profite - 60) * 0.015
# elif(60 >= profite > 40):
#     rate = 40 * 0.1 + (profite - 40) * 0.03
# elif(40 >= profite > 20):
#     rate = 20 * 0.1 + (profite - 20) * 0.05
# elif(20 >= profite > 10):
#     rate = 10 * 0.1 + (profite - 10) * 0.075
# else:
#     rate =  profite * 0.1
#
# print("奖金%.4f(万元)"%rate)


i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        #print (i-arr[idx])*rat[idx]
        i=arr[idx]
print(r)