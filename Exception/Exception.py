try:
    file = open("D:\exception.txt", "r", encoding="UTF-8")
except Exception as e:
    file = open("D:\exception.txt", "w", encoding="UTF-8")
    print(f"捕获到异常-->{e}")
else:
    print("没有异常出现呢~")
finally:
    print("管他有没有异常")
