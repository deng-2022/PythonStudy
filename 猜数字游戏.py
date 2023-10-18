from random import *

Q = randint(0, 9)
while True:
    N = eval(input("输入你猜的数字:"))
    if N == Q:
        print("猜对啦!正确数字是{}。".format(Q))
        break
    elif N >= Q:
        print("数字太大了!")
    else:
        print("数字太小了!")
