from pyecharts.charts import Map
from pyecharts.globals import ChartType, ThemeType
from pyecharts import options as opts

# 准备地图对象
map_japan = Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

# 准备数据
data = [("北海道", 10), ("青森県", 15), ("岩手県", 20), ("宮城県", 25), ("秋田県", 30),
        ("山形県", 35), ("福島県", 40), ("茨城県", 11), ("栃木県", 16), ("群馬県", 21),
        ("埼玉県", 26), ("千葉県", 31), ("東京都", 36), ("神奈川県", 41), ("新潟県", 12),
        ("富山県", 17), ("石川県", 22), ("福井県", 27), ("山梨県", 32), ("長野県", 37),
        ("岐阜県", 42), ("静岡県", 13), ("愛知県", 18), ("三重県", 23), ("滋賀県", 28),
        ("京都府", 33), ("大阪府", 38), ("兵庫県", 43), ("奈良県", 14), ("和歌山県", 19),
        ("鳥取県", 24), ("島根県", 29), ("岡山県", 34), ("広島県", 39), ("山口県", 44),
        ("徳島県", 25), ("香川県", 30), ("愛媛県", 35), ("高知県", 40), ("福岡県", 45),
        ("佐賀県", 10), ("長崎県", 15), ("熊本県", 20), ("大分県", 25), ("宮崎県", 30),
        ("鹿児島県", 35), ("沖縄県", 40)]

# 添加数据
map_japan.add("", data, maptype="japan")

# 设置全局选项
map_japan.set_global_opts(
    title_opts=opts.TitleOpts(title="日本地图示例"),
    visualmap_opts=opts.VisualMapOpts(is_piecewise=True, max_=50, min_=10)
)

# 绘图并保存
map_japan.render("japan_map.html")