# 爬取https://www.bilibili.com/video/BV1ha4y1H7sx?p=6&vd_source=4314e5bd742ea904c9675af8a6b4b07e/
import requests

if __name__ == '__main__':
    # 指定url
    url = "https://js.design/?source=itab&plan=1"
    # 发起请求
    response = requests.get(url=url)
    # 接收响应
    page_text = response.text
    # 持久化存储
    print(page_text)
    with open("baidu.html", "w", encoding="utf-8") as fp:
        fp.write(page_text)
    print("爬取数据结束!!")
