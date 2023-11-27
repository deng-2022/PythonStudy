import requests

api_url = "https://api.zhihu.com/columns"
params = {
    "limit": 10,
    "offset": 0
}

try:
    for i in range(2):  # 获取2页数据，每页10个专栏
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", [])
            for item in data:
                column_id = item.get("id")
                column_title = item.get("title")
                column_url = item.get("url")
                print(f"专栏标题: {column_title}, 专栏ID: {column_id}")
            params["offset"] += params["limit"]
        else:
            print("无法获取专栏列表")
            break

except requests.RequestException as e:
    print("请求异常:", repr(e))