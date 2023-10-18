from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
from pyecharts import options as opts

# 准备地图对象
map = Map(init_opts=opts.InitOpts(width="2000px",height="1000px"))
# 准备数据
data = [
    ("北京市", 99),
    ("山西省", 12),
    ("湖南省", 456),
    ("上海市", 1000),
    ("新疆维吾尔自治区", 1369)
]
# 添加数据
map.add("中国地图", data, "china")
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#CCFFFF"},
            {"min": 501, "max": 1500, "label": "501-1500", "color": "#CCFFFF"}
        ]
    )
)
# 绘图
map.render("china.html")
