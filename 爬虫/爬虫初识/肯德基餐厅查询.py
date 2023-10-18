import requests
import json

if __name__ == '__main__':
    # url路径
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
    }
    # 请求参数
    content = input('输入要查询的地点:')
    data = {
        'cname': '',
        'pid': '',
        'keyword': content,
        'pageIndex': '1',
        'pageSize': '10'
    }
    # 发送请求
    response = requests.post(url=url, data=data, headers=headers)
    # 获取响应
    dic_text = response.text
    # 持久化存储l
    filename = content + '.text'
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_text, fp, ensure_ascii=False)
    print('over!!!')
