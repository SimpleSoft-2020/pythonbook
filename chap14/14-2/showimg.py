import sys
import cv2
img = cv2.imread("test.jpg")
if img is None:
    sys.exit("Can not read the image test.jpg.")
cv2.imshow("image",img)
key = cv2.waitKey()

    