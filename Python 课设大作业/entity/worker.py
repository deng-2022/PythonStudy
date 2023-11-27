# 声明一个类
# 3. 新增职工实体类 Worker，并使用该实体类列表接收查询到的职工数据记录
class Worker:
    def __init__(self, id, name, age, position):
        self.id = id
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"{self.id} {self.name} {self.age} {self.position}"



