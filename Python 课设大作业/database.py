# 数据库连接模块
import mysql.connector

# 创建数据库连接
cnx = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    port="3306",  # 数据库端口号
    user="root",  # 数据库用户名
    password="Dw990831",  # 数据库密码
    database="memory_search"  # 数据库名称
)

cursor = cnx.cursor()

# 执行查询语句
cursor.execute("SELECT * FROM article")

# 获取查询结果
results = cursor.fetchall()

# 处理查询结果
for row in results:
    print(row)
