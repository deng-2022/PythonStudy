import os.path

import requests
from lxml import etree

if __name__ == '__main__':
    # url路径
    url = 'https://bobopic.com/4kbizhi.html'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/72.0.3626.121 Safari/537.36'
    }
    # 请求页面
    page_text = requests.get(url=url, headers=headers).text
    # 封装页面对象
    tree = etree.HTML(page_text)
    # 获取a标签
    a_list = tree.xpath('//div[@class="related"]/ul/li/a')
    # 遍历a_list
    for a in a_list:
        # 拿取每个a的href
        a_href = a.xpath('./@href')[0]
        # 请求新页面
        new_page_text = requests.get(url=a_href + '', headers=headers).content
        # 封装页面对象
        tree = etree.HTML(new_page_text)
        img_list = tree.xpath('//div[@class="entry-content u-clearfix"]//img')
        if not os.path.exists('./二次元风景4k'):
            os.mkdir('./二次元风景4k')
        # 获取新页面下的图片
        for img in img_list:
            # 图片名
            img_name = img.xpath('./@alt')[0] + '.jpg'
            # 图片路径
            img_src = img.xpath('./@src')[0] + ''
            # 爬取图片
            img_data = requests.get(url=img_src, headers=headers).content
            # 图片存放路径
            img_path = '二次元风景4k/' + img_name
            # 存放图片
            with open('二次元风景4k/' + img_name, 'wb') as fp:
                fp.write(img_data)
            print(img_name + '下载成功！')
