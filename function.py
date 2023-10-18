# 查询余额
def select_money():
    print(f"尊敬的{name}先生,您的余额剩余:{money}元")


# 存款
def deposit():
    num = int(input("请输入要存款的额度:"))
    global money
    money += num
    print(f"存款成功!当前余额为:{money}")


# 取款
def withdrawal():
    num = int(input("请输入要取款的额度:"))
    global money
    money -= num
    print(f"取款成功!当前余额为:{money}")


# 退出
def exist():
    print("谢谢您的使用,欢迎下次再来!")
    print("系统正在退出...")
    global flag
    flag = False


money = 50000
flag = True


name = input("您好,请问您尊姓大名?")
while flag:
    print(f"尊敬的{name}先生,请选择业务需求:")
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    select = int(input("请输入您的选择:"))

    if select == 1:
        select_money()

    elif select == 2:
        deposit()

    elif select == 3:
        withdrawal()

    elif select == 4:
        exist()

    else:
        print("您他娘的输错啦!")
