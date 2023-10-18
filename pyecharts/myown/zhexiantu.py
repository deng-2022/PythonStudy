"""
演示可视化需求1：折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts

f_us = open("D:/Project/python/other/美国.txt", "r", encoding="UTF-8")
# 获取数据
us_data = f_us.read()
# 处理数据
# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]
# JSON转Python字典
us_dict = json.loads(us_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
# 获取确认数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data']
# 生成图表
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data)
# 添加y轴数据
line.add_yaxis("美国新冠死亡人数", us_y_data)
# 设置全局选项
# line.set_global_opts(
#     # 标题设置
#     title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
# )
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2023年美国各项原因致死亡人数预测折线图", pos_left="center", pos_bottom="1%")
)

# 调用render方法，生成图表
line.render()
# 关闭文件对象
f_us.close()
