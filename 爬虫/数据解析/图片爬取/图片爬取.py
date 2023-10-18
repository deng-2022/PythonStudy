# https://5b0988e595225.cdn.sohucs.com/images/20180223/7867cff3355848f09a29a2f481288218.jpeg
# 爬取并存储一张图片
import requests

if __name__ == '__main__':
    # url路径
    url = 'https://dl.bobopic.com/small/69243761.jpg'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
    }
    # 发送请求
    # 获取响应数据 text 字符串 content 二进制  json 对象
    img_data = requests.get(url=url, headers=headers).content
    # 持久化存储 写入方式为 'wb'
    with open('米饭.jpg', 'wb') as fp:
        fp.write(img_data)
    print('over!!!')
