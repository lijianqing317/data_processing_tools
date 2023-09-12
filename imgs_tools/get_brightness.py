# author
# 把图片转换为单通道的灰度图
import cv2
import numpy as np
img = cv2.imread('/home/adt/Desktop/test/1647-0007-202.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 获取形状以及长宽
img_shape = gray_img.shape
height, width = img_shape[0], img_shape[1]
size = gray_img.size
# 灰度图的直方图
hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

# 计算灰度图像素点偏离均值(128)程序
a = 0
ma = 0
reduce_matrix = np.full((height, width), 128)
shift_value = gray_img - reduce_matrix
shift_sum = sum(map(sum, shift_value))

da = shift_sum / size
# 计算偏离128的平均偏差
for i in range(256):
    ma += (abs(i - 128 - da) * hist[i])
m = abs(ma / size)
# 亮度系数
k = abs(da) / m
# print(k)
if k[0] > 1:
    # 过亮
    if da > 0:
        print("过亮")
    else:
        print("过暗")
else:
    print("亮度正常")
import PIL.ImageEnhance
import PIL.Image
import PIL.ImageEnhance
import os
pathimg = '/home/adt/Desktop/test/'
save_path = '/home/adt/Desktop/test_r'
for i in os.listdir(pathimg):
    imagep = os.path.join(pathimg,i)
    savep = os.path.join(save_path,i)
    img = PIL.Image.open(imagep)
    print(img.format)
    img1 = PIL.ImageEnhance.Brightness(img).enhance(1.5)
    img1.show()
    img1.save(savep, quality=95)
# cv2.imshow("图片1", img)
# cv2.imshow("图片2", img1)
# cv2.waitKey()
# cv2.destroyAllWindows()
