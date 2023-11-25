import pandas as pd
from pandas import DataFrame


def test1():
    # 读取Excel文件
    df = pd.read_excel('职工表.xlsx')
    # 打印数据框的内容
    print(df)


def test2():
    data = pd.read_excel('职工表.xlsx', sheet_name='Sheet1')
    print(data)
    print('--------------------------')

    # 增加行数据，在第5行新增
    data.loc[4] = ['4', 'john', 'pandas']

    # 增加列数据，给定默认值None
    data['new_col'] = None

    # 保存数据
    DataFrame(data).to_excel('new.xlsx', sheet_name='Sheet1', index=False, header=True)


if __name__ == '__main__':
    test2()
