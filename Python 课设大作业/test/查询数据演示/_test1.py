# 数据库连接模块
import mysql.connector
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# 创建数据库连接
cnx = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    port="3306",  # 数据库端口号
    user="root",  # 数据库用户名
    password="Dw990831",  # 数据库密码
    database="python_work"  # 数据库名称
)

cursor = cnx.cursor()

# 执行查询语句
cursor.execute("SELECT * FROM worker")

# 获取查询结果
results = cursor.fetchall()

print(f'查询结果:{results}')


# 3. 新增职工实体类 Worker，并使用该实体类列表接收查询到的职工数据记录
class Worker:
    def __init__(self, id, name, age, position):
        self.id = id
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"{self.id} {self.name} {self.age} {self.position}"


# workers = [Worker(row[0], row[1], row[2], row[3]) for row in results]

workers = []
for row in results:
    worker = Worker(row[0], row[1], row[2], row[3])
    workers.append(worker)

# 4. 打印职工记录
for worker in workers:
    print(worker)

# 提取每个Worker的信息
worker_info = []
for worker in workers:
    name = worker.name
    age = worker.age
    position = worker.position
    worker_info.append((name, age, position))

# 绘制柱状图
# labels, ages, positions = zip(*worker_info)
# plt.bar(labels, ages, label='Age')
# plt.bar(labels, positions, label='Position')
# plt.xlabel('Name')
# plt.ylabel('Value')
# plt.title('Worker Information')
# plt.legend()
# plt.show()

# 创建柱状图
fig = make_subplots(rows=1, cols=2)

# 添加年龄数据到图表
fig.add_trace(go.Bar(x=[worker[0] for worker in worker_info], y=[worker[1] for worker in worker_info], name='年龄'), row=1, col=1)

# 添加职位数据到图表
fig.add_trace(go.Bar(x=[worker[0] for worker in worker_info], y=[worker[2] == '经理' for worker in worker_info], name='职位'), row=1, col=2)

# 更新布局
fig.update_layout(title='工人信息', xaxis_title='姓名', yaxis_title='数量')

# 显示图表
fig.show()

# 关闭数据库连接
cursor.close()
cnx.close()
