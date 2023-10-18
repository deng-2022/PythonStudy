import json

import requests

if __name__ == '__main__':
    # url路径
    url = "https://api.codelife.cc/api/getWeather"
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/113.0.0.0'
    }
    # 请求参数
    params = {
        'lang': ' cn',
        'location': '101101101'
    }
    # 发送请求
    response = requests.get(url, params=params, headers=headers)
    # 获取响应
    dic_obj = response.json()
    # 持久化存储
    fp = open('iTab标签页.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp, ensure_ascii=False)
    print('over!!!')
