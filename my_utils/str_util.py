# 接受传入字符串, 将字符串反转后返回
def str_reverse(s):
    return s[::-1]


# 按照下标x和y, 对字符串进行切片
def substr(s, x, y):
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("几把程序员"))
    print(substr("啊u覅与阿尔", 1, 3))
