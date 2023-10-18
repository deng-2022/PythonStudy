print("打印九九乘法表:")

i = 0
while i < 10:
    j = 1
    while j <= i:
        # print("%d * %d = %d  " % (j, i, i * j), end='')
        num = i * j
        print(f"{j} * {i} = {num}  ", end='')
        j += 1
    i += 1
    print("")
print("打印完成!")
