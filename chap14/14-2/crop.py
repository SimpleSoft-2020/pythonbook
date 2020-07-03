import sys
import cv2
img = cv2.imread("test.jpg")
if img is None:
    sys.exit("Can not read the image test.jpg.")
height, width = img.shape[0:2]
crop = img[0:(int)(height/2), 0:(int)(width/2)]
#show the image
cv2.imshow("crop",crop)
#save the image
cv2.imwrite("crop.jpg",crop)
cv2.waitKey(0)

