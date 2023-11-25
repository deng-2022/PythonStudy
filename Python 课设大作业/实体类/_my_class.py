# 声明一个类
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")


if __name__ == '__main__':
    # 实例化一个对象
    my_object = MyClass("张三")
    # 调用对象的方法
    my_object.say_hello()
