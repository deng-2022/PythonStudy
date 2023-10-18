import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# 定义数据点和相应的类别标签
points = np.array([[1.51, 0.60], [1.42, 1.50], [1.73, 0.93], [0.99, 0.64],
                  [2.48, 1.67], [2.26, 0.88], [1.98, 0.70], [1.98, 0.85],
                  [3.57, 1.59], [3.43, 0.53], [5.26, 0.13], [4.82, 0.47],
                  [4.15, 1.36], [3.37, 1.39], [3.56, 1.42], [3.91, 1.13],
                  [2.39, 3.61], [2.06, 2.54], [2.73, 3.73], [1.61, 3.43],
                  [2.52, 3.06], [1.87, 3.02], [2.13, 2.99], [2.57, 2.94],
                  [3.81, 2.28], [3.82, 3.27], [4.21, 2.95], [4.56, 2.86],
                  [4.03, 3.05], [3.69, 2.93], [4.11, 2.32], [3.89, 2.71]])

labels = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
                   2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3])

# 创建KNN分类器对象
knn = KNeighborsClassifier(n_neighbors=3)

# 拟合数据
knn.fit(points, labels)

# 预测测试点的类别标签
test_point = np.array([[1.52, 2.15]])
predicted_label = knn.predict(test_point)

print("测试点的类别标签是:", predicted_label)

# 绘制数据点和决策平面
h = 0.01
x_min, x_max = points[:, 0].min() - 1, points[:, 0].max() + 1
y_min, y_max = points[:, 1].min() - 1, points[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# 绘制数据点
for i in range(4):
    plt.scatter(points[labels == i][:, 0], points[labels == i][:, 1], cmap=plt.cm.Paired, edgecolor='k')

plt.scatter(test_point[:, 0], test_point[:, 1], color='k', marker='x', label="Test Point")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Decision Boundary')
plt.legend()
plt.show()