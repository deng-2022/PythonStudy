from pyecharts.charts import Map
from pyecharts import options as opts

# 创建地图对象
china_map = Map()

# 准备数据
province_data = [
    ("广东省", 100),
    ("北京市", 506),
    ("上海市", 88),
    ("山西省", 1000),
    # 其他省份数据...
]

# 设置地图数据
china_map.add("中国地图", province_data, "china")

# 设置全局选项
china_map.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#99CCFF"},
            {"min": 501, "max": 1500, "label": "501-1500", "color": "#66CCFF"}
        ]
    )
)

# 绘图并保存
china_map.render("china_map.html")