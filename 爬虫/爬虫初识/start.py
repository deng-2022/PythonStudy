# 爬取百度搜索页面数据 https://m.baidu.com/
import requests

if __name__ == '__main__':
    # 指定url
    url = "https://m.baidu.com/"
    # 发起请求
    response = requests.get(url=url)
    # 接收响应
    page_text = response.text
    # 持久化存储
    print(page_text)
    with open("baidu.html", "w", encoding="utf-8") as fp:
        fp.write(page_text)
    print("爬取数据结束!!")
