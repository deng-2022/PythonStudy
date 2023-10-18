import os.path
import re
import requests

if __name__ == '__main__':
    # 创建文件夹
    if not os.path.exists('./imgs'):
        os.mkdir('./imgs')
    # 请求路径
    url = 'https://www.woyaogexing.com/tupian/index_%d.html'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/113.0.0.0'
    }
    for page_num in range(1, 11):
        new_url = format(url % page_num)
        # 爬取对应的网页内容
        page_text = requests.get(url=new_url, headers=headers).text
        # print(page_text)
        # 爬取对应网页上的图片(正则表达式)
        # 编写正则表达式
        ex = '<div class="txList ">.*?<img.*?src="(.*?)".*?>.*?</div>'
        # 获取所需字符串
        img_src_list = re.findall(ex, page_text, re.S)
        print(img_src_list)
        for img_src in img_src_list:
            # 拼接完整的图片路径
            img_src = 'http:' + img_src
            print(img_src)
            # 请求图片
            img = requests.get(url=img_src, headers=headers).content
            # 图片名
            img_name = img_src.split('/')[-1]
            # 图片保存路径
            img_path = './imgs/' + img_name
            print('img_path = ' + img_path)
            # 保存图片
            with open(img_path, 'wb') as fp:
                fp.write(img)
            print(img_name + '下载完成！')
        print('over!!!')
