import requests

if __name__ == '__main__':
    # UA伪装: 爬虫对应的身份标识伪装成某一浏览器, 避免请求被拒绝
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/113.0.0.0'
    }
    # 请求路径
    url = 'https://www.sogou.com/web?'
    # 请求参数
    content = input('输入搜索词:')
    params = {
        'query': content
    }
    # 发送请求
    response = requests.get(url=url, params=params, headers=headers)
    # 获取响应值
    page_text = response.text
    # 持久化存储
    fileName = content + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '抓取成功!')
