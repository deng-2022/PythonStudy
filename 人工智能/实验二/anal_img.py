import numpy as np
import matplotlib.pyplot as plt

# 读取照片
image = plt.imread('number.jpg')

# 显示照片
plt.imshow(image)
plt.axis('off')
plt.show()