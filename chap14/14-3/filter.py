from PIL import Image
from PIL import ImageFilter

img = Image.open("test.jpg")
blur = img.filter(ImageFilter.BLUR)
blur.show("模糊")
#轮廓检测
counter = img.filter(ImageFilter.CONTOUR)
counter.show("轮廓")
#边沿增强
edge = img.filter(ImageFilter.EDGE_ENHANCE)
edge.show("边沿增强")
#浮雕
emboss = img.filter(ImageFilter.EMBOSS)
emboss.show("浮雕")
#锐化
sharpen = img.filter(ImageFilter.SHARPEN)
sharpen.show("锐化")
#平滑
smooth = img.filter(ImageFilter.SMOOTH)
smooth.show("平滑")


