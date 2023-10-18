file_read = open("D:/itheima.txt", "r", encoding="UTF-8")
file_write = open("D:/good.txt", "a", encoding="UTF-8")

for line in file_read:
    line = line.strip()
    _line = line.split(",")

    if _line[1] == "测试":
        continue
    else:
        file_write.write(f"{line}\n")

