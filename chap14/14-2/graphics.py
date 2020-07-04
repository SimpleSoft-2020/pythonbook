import numpy
import cv2
#构建一个画布，大小为1024*768，默认为黑色
img = numpy.zeros((768, 1024, 3), numpy.uint8)
#绘制一个矩形，把画布变为白色
cv2.rectangle(img,(0,0),(1024,768),(255,255,255),-10)
#绘制圆
cv2.circle(img,(110,110),100,(0,0,255),10,cv2.LINE_4)
#绘制圆，用抗锯齿线
cv2.circle(img,(200,200),100,(255,0,0),10,cv2.LINE_AA)
#绘制实心椭圆，绿色
cv2.ellipse(img,(340,340),(100,80), 90, 0, 360,(0,255,0),-1)
#绘制直线
cv2.line(img, (350,50), (350,200), (255,255,0),10)
#绘制带箭头直线
cv2.arrowedLine(img, (350,50), (500,50), (255,0,255),10,tipLength=.2)
#输出文字
cv2.putText(img,"OpenCV",(420,400),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))
cv2.imshow("img",img)
key = cv2.waitKey()
