import numpy as np

def matrix_alg():
    # 定义矩阵 A 和 B
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("矩阵A：\n", A)
    print("矩阵B：\n", B)

    # 矩阵加法
    add = A + B
    print("矩阵加法结果：\n", add)

    # 矩阵减法
    sub = A - B
    print("矩阵减法结果：\n", sub)

    # 矩阵乘法（数乘矩阵）
    mul = 2 * A
    print("数乘矩阵结果：\n", mul)

    # 矩阵乘法（矩阵对应元素相乘）
    mul_elem = A * B
    print("矩阵对应元素相乘结果：\n", mul_elem)

    # 矩阵乘法（两个矩阵相乘）
    mul_mat = np.dot(A, B)
    print("两个矩阵相乘结果：\n", mul_mat)


# 提取矩阵中相应元素
def mat_get_elem():
    # 定义矩阵 A
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("矩阵A：\n", A)

    # 提取矩阵中的元素
    mul_mat = A[0, 0]
    print("第一个元素：", mul_mat)

    # 提取第一行元素
    first_row = A[0, :]
    print("第一行元素：", first_row)

    # 提取第二列元素
    second_column = A[:, 1]
    print("第二列元素：", second_column)

    # 计算第一行元素与第二列元素相加的结果
    result = A[0, :] + A[:, 1]
    print("第一行元素与第二列元素相加的结果：", result)

# 矩阵形状变化
def mat_change():
    # 定义矩阵 A
    A = np.array([[1, 2, 3], [4, 5, 6]])
    print("矩阵A：\n", A)

    # 矩阵转置
    trans_A = np.transpose(A)
    print("矩阵转置：")
    print(trans_A)

    # 按行拉直为列向量
    row_vector = A.reshape(-1, 1)
    print("按行拉直为列向量：")
    print(row_vector)

    # 按列拉直为列向量
    column_vector = A.reshape(1, -1)
    print("按列拉直为列向量：")
    print(column_vector)

    # 计算矩阵的大小（行数、列数）
    rows, cols = A.shape
    print("矩阵大小（行数、列数）：", rows, cols)


if __name__ == '__main__':
    # matrix_alg()
    # mat_get_elem()
    mat_change()