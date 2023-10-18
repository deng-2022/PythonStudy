import requests
import json

id_list = []  # 获取每个企业的id
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
}
# url请求路径
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
# 发送请求
# 拿取 1-19 页
for page in range(1, 20):
    page = str(page)
    # 请求参数
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }
    # 以json的格式返回response的内容（如果有的话）
    response = requests.post(url=url, headers=headers, data=data).json()
    for dic in response['list']:  # response是一个字典，list是一个键，而我们需要这个键对应的值，所以就有了`response['list'],
        # 稍微复杂的是dic是一个数组，这个数组里包括了一部字典，
        id_list.append(dic['ID'])  # dic是一个字典，我们同样用‘ID’这个键访问它对应的值，并把这个值添加到id_list[]里

# 从这里开始整个程序分为两部分，上面是获取所有的id，下面是对所有的id信息进行请求，然后是保存。
all_data = []  # 这个列表用来存放最终的所有公司的具体信息
# url请求路径
post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
# 发送请求
for id in id_list:  # 把id封装到字典当作作为参数以备调用
    # 请求参数
    data2 = {  # 遍历所有的id
        'id': id
    }
    result = requests.post(url=post_url, headers=headers, data=data2).json()
    all_data.append(result)  # 通过a数据解析append方法把所有的请求结果上传到all_data[]中
    print(result)  # 直接输出请求返回的结果

# 持久化存储
file = open('./化妆品生产许可信息.json', 'w', encoding='utf-8')
json.dump(all_data, fp=file, ensure_ascii=False)
