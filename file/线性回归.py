import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 定义年份和单价的数据
    years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013])
    prices = np.array(
        [2.000, 2.500, 2.900, 3.147, 4.515, 4.903, 5.365, 5.704, 6.853, 7.971, 8.561, 10.000, 11.280, 12.900])

    # 将年份转为二维数组，以便进行线性回归拟合
    X = years.reshape((-1, 1))

    # 创建线性回归模型对象
    model = LinearRegression()

    # 拟合数据
    model.fit(X, prices)

    # 预测全部数据
    predicted_prices = model.predict(X)

    # 绘制拟合曲线和原始数据
    plt.plot(years, predicted_prices, label='Linear Regression')
    plt.scatter(years, prices, color='red', label='Original data')

    # 添加图例、标题和坐标轴标签
    plt.legend()
    plt.title('Housing Price and Year in Nanjing')
    plt.xlabel('Year')
    plt.ylabel('Price')

    # 显示图形
    plt.show()
