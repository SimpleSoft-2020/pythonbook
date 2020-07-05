from PIL import Image
img = Image.open("test.jpg")
#旋转45度
rotate45 = img.rotate(45)
rotate45.show()
#旋转270度
rotate270 = img.rotate(270)
rotate270.show()
#左右镜像
flip=img.transpose(Image.FLIP_LEFT_RIGHT)
flip.show()
#上下镜像
flip2=img.transpose(Image.FLIP_TOP_BOTTOM)
flip2.show()
