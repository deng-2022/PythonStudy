i = 0
num = 0
with open("D:\itheima.txt", "r", encoding="UTF-8") as file:
    append = open("D:\itheima.txt", "a", encoding="UTF-8")
    for line in file:
        line = line.strip()
        line = line.split(" ")

        num += line.count("itheima")

        i += 1
        print(f"文件第{i}行为:{line}")

    append.write("\n你看得懂中文不?")
    append.flush()
    # append.close()

    print(f"共有{num}个itheima")
    
