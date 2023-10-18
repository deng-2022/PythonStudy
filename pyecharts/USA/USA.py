from pyecharts.charts import Map


# 创建地图对象
usa_map = Map()

# 设置地理数据
# 这里假设你已经下载了 USA.json 文件作为地理数据文件
usa_map.add("", [], "USA", json_file="USA.json")

# 设置全局选项和数据
# 这里假设你已经准备好了要显示在地图上的数据
usa_map.set_global_opts(
    title_opts={"text": "USA Map"},
    visualmap_opts={"min": 0, "max": 1000}
)

# 绘图并保存
usa_map.render("usa_map.html")

# # 绘图并保存
# usa_map.render("usa_map.html")
#
# {
#     "type": "FeatureCollection",
#     "features": [
#         {
#             "type": "Feature",
#             "id": "01",
#             "properties": {
#                 "name": "Alabama"
#             },
#             "geometry": {
#                 "type": "Polygon",
#                 "coordinates": [
#                     [
#                         [
#                             -87.359296,
#                             35.00118
#                         ],
#                         [
#                             -85.606675,
#                             34.984749
#                         ],
#                         [
#                             -85.431413,
#                             34.124869
#                         ],