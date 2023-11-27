# 导入必要的包
import cv2

# 读入要检测的图像
face_image = cv2.imread("pic1.JPG")
# face_image = cv2.imread("pic2.JPG")

# 加载人脸检测器
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 人脸检测
faces = face_model.detectMultiScale(face_image, 1.3)
print(faces)

# 绘制矩形框
for (x, y, w, h) in faces:
    cv2.rectangle(face_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 显示图像
cv2.imshow("detection result", face_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
