import cv2
img = cv2.imread('fliptest.jpg')
height, width = img.shape[0:2]
#旋转45度
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, .5)
rotate45 = cv2.warpAffine(img, matrix, (width, height))
#旋转-45度
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), -45, 1)
rotate315 = cv2.warpAffine(img, matrix, (width, height))
cv2.imshow('img', img)
cv2.imshow('rotate45', rotate45) 
cv2.imshow('rotate315', rotate315) 
cv2.waitKey(0)
cv2.destroyAllWindows()

