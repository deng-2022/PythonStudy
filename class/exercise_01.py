class Student:

    def __str__(self) -> str:
        return super().__str__()

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


def print_student():
    for i in students:
        print(i.name)
        print(i.age)
        print(i.address)


num = [1, 2, 3]
students = []

stu = Student("灯火辉煌", 100, "案发现场")
print(stu.__str__())

for i in num:
    input(f"当前录入第{i}位同学的信息,总共需录入{len(num)}位同学的信息")

    name = input("请输入学生姓名:")
    age = input("请输入学生年龄:")
    address = input("请输入学生地址:")

    student = Student(name, age, address)

    students.append(student)

    print(f"学生{i}信息录入完成,信息为: {student.name},{student.age},{student.address}")

print(f"输出所有学生信息:")
print_student()
