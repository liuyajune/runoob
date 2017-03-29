#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。

程序分析：无。
'''
import random
import time
if __name__ == '__main__':
    play_it = input('do you want to play (\'y\' or \'n\')')
    while play_it == 'y':
        number = random.randint(10, 20)
        guess = int(input('input your number:'))
        start = time.clock()
        while guess != number:
            if guess > number:
                print("bigger")
                #guess = int(input('try again:'))
            elif guess < number:
                print('smaller')
            guess = int(input('try again:'))
        end = time.clock()
        var = end - start
        if var >= 15:
            print("very good")
        elif  15 > var > 10:
            print('very very good')
        else:
            print('super')

    play_it = input('do you want to play')