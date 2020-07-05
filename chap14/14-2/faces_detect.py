import cv2
#创建一个CascadeClassifier
cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#读取face.png文件
img=cv2.imread('face.png')
#人脸检测
faces=cascade.detectMultiScale(img,scaleFactor=1.5,minNeighbors=6)
#对检测出来的脸进行标记，绘制一个矩形
for x,y,w,h in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow("img",img)
cv2.waitKey(0)

