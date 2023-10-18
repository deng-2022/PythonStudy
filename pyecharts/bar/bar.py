from pyecharts.charts import Bar
from pyecharts import options as opts

# 准备柱状图数据
x_data = ["A", "B", "C", "D"]
y_data = [10, 20, 30, 40]

# 创建柱状图对象
bar = Bar(init_opts=opts.InitOpts(width="1000px"))

# 添加x轴数据
bar.add_xaxis(x_data)

# 添加y轴数据
bar.add_yaxis("柱状图", y_data)

# 设置全局选项
bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图示例"))

# 绘图并保存
bar.render("bar_chart.html")