﻿import cv2
#读取原始图像
img = cv2.imread("blur_test.jpg")
#使用归一化滤波方式进行模糊
blur_img =cv2.blur(img,(9,9)) 
#显示原始图像
cv2.imshow("img",img)
#显示模糊后的图像
cv2.imshow("blur_img",blur_img)
cv2.waitKey(0)

