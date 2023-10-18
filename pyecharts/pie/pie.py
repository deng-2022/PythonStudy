from pyecharts.charts import Pie
from pyecharts import options as opts

# 准备饼图数据
data = [
    ("吃饭", 30),
    ("睡觉", 20),
    ("打豆豆", 50)
]

# 创建饼图对象
pie = Pie(init_opts=opts.InitOpts(width="1000px"))

# 添加数据
pie.add("", data)

# 设置全局选项
pie.set_global_opts(title_opts=opts.TitleOpts(title="饼图示例"))

# 绘图并保存
pie.render("pie_chart.html")
