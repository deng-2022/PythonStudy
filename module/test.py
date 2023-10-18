__all__ = ['hello', 'hihi']  # 指定能够使用的方法


def hello():
    print("??????")


if __name__ == '__main__':  # 指定不能使用的方法
    def hi():
        print("啥!")


def hihi():
    print("hi和hi")


hello()
