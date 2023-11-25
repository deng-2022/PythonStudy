from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 加载MNIST数据集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 预处理照片
train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255

# 归一化数据
train_images = train_images - np.mean(train_images)
test_images = test_images - np.mean(train_images)

# 将标签转换为分类编码
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 构建神经网络模型
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(train_images, train_labels, epochs=10, batch_size=64)

# 评估模型性能
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# 读取手写数字图像
image = Image.open('number.jpg').convert('L')  # convert to grayscale

# 调整图像大小
image = image.resize((28, 28))

# 将图像数据转换为numpy数组
image = np.asarray(image)

# 将图像数据归一化到 0-1 范围
image = image / 255.0

# 使用模型对图像进行预测
predictions = model.predict(image.reshape((1, 28, 28, 1)))

# 获取预测的数字标签
predicted_label = np.argmax(predictions, axis=1)[0]

# 获取对应的数字标签文本
label_text = 'number =  ' + str(predicted_label)

# 显示图像和对应的数字标签文本
plt.imshow(image)
plt.title(label_text)
plt.axis('off')
plt.show()
