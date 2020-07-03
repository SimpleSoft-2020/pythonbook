import sys
import cv2
img = cv2.imread("test.jpg")
if img is None:
    sys.exit("Can not read the image test.jpg.")
x, y = img.shape[0:2]
cv2.imshow("image",img)
imgzoomout = cv2.resize(img, (int(y / 2), int(x / 2)))
imgzoomin = cv2.resize(img, (int(y * 2), int(x * 2)))
cv2.imshow("imgzoomout",imgzoomout)
cv2.imshow("imgzoomin",imgzoomin)
key = cv2.waitKey()