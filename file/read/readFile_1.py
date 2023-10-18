i = 1
num = 0
itheima = "itheima"
itheima2 = "itheima\n"
with open("D:\itheima.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line = line.split(" ")

        for _line in line:
            if itheima == _line or itheima2 == _line:
                num += 1

        print(f"第{i}行数据:{line}")

        i += 1
    print(f"一共出现了{num}次itheima")
