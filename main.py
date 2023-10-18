import random

guess_num = random.randint(1, 10)

num = int(input("您老猜猜这个数是多少?"))

if num > 10 | num < 1:
    print("啧啧啧,不长眼睛吗?让你猜1-10之间的数!")

elif num > guess_num:
    print("大了!")
    num = int(input("你老再猜猜看,是多少呢?"))
    if num > guess_num:
        print("大了!")
        num = int(input("最后一次机会了,到底是多少呢?"))
        if num > guess_num:
            print("结束了!沙雕一个,这都没猜中,是%d!没想到吧!" % guess_num)

        elif num < guess_num:
            print("结束了!沙雕一个,这都没猜中,是%d!没想到吧!" % guess_num)

        else:
            print("他娘的真是个天才,答案正是%d" % guess_num)

    elif num < guess_num:
        print("小了!")
        num = int(input("最后一次机会了,到底是多少呢?"))
        if num > guess_num:
            print("结束了!沙雕一个,这都没猜中,是%d!没想到吧!" % guess_num)

        elif num < guess_num:
            print("结束了!沙雕一个,这都没猜中,是%d!没想到吧!" % guess_num)

        else:
            print("他娘的真是个天才,答案正是%d" % guess_num)

    else:
        print("他娘的真是个天才,答案正是%d" % guess_num)

elif num < guess_num:
    print("小了!")
    num = int(input("你老再猜猜看,是多少呢?"))
    if num > guess_num:
        print("大了!")
        num = int(input("最后一次机会了,到底是多少呢?"))
        if num > guess_num:
            print("结束了!沙雕一个,这都没猜中,是%d!没想到吧!" % guess_num)

        elif num < guess_num:
            print("结束了!沙雕一个,这都没猜中,是%d!没想到吧!" % guess_num)

        else:
            print("他娘的真是个天才,答案正是%d" % guess_num)

    elif num < guess_num:
        print("小了!")
        num = int(input("最后一次机会了,到底是多少呢?"))
        if num > guess_num:
            print("结束了!沙雕一个,这都没猜中,是%d!没想到吧!" % guess_num)

        elif num < guess_num:
            print("结束了!沙雕一个,这都没猜中,是%d!没想到吧!" % guess_num)

        else:
            print("他娘的真是个天才,答案正是%d" % guess_num)

    else:
        print("他娘的真是个天才,答案正是%d" % guess_num)

else:
    print("他娘的真是个天才,答案正是%d" % guess_num)