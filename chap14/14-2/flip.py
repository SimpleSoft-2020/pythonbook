import cv2
img = cv2.imread("fliptest.jpg")
if img is None:
    sys.exit("Can not read the image fliptest.jpg.")
#垂直翻转
flip0 = cv2.flip(img,0)
#水平翻转
flip1 = cv2.flip(img,1)
#垂直+水平翻转
flip2 = cv2.flip(img,-1)
cv2.imshow("img",img)
cv2.imshow("flip0",flip0)
cv2.imshow("flip1",flip1)
cv2.imshow("flip2",flip2)
cv2.waitKey(0)
