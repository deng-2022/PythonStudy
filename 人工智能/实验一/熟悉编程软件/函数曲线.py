import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x):
    return np.sin(x)


if __name__ == '__main__':
    # 定义x的范围
    x = np.linspace(0, 2 * np.pi, 100)

    # 绘制函数曲线
    plt.plot(x, f(x), linestyle='--', linewidth=2, color='red', label='Function Curve')

    # 绘制散点图
    x_scatter = np.linspace(0, 2 * np.pi, 10)
    y_scatter = f(x_scatter)
    plt.scatter(x_scatter, y_scatter, marker='o', color='blue', label='Scatter Plot')

    # 添加图例
    plt.legend()

    # 添加标题和坐标轴标签
    plt.title('Function Curve and Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')

    # 显示图形
    plt.show()
