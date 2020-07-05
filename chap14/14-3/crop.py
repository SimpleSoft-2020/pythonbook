from PIL import Image
import os, sys
img = Image.open("test.jpg")
#获取图像的宽和高
width,height = img.size
crop_width=width/2
crop_height=height/2
#分成四个矩形
img1_box = (0,0,width / 2,height / 2)
img2_box = (width /2,0,width/2+crop_width,height/2)
img3_box=(0,height/2,crop_width,height/2 + crop_height)
img4_box = (width/2,height/2,width/2+crop_width,height/2+crop_height)
#裁剪四个图像
img1 = img.crop(img1_box)
img2 = img.crop(img2_box)
img3 = img.crop(img3_box)
img4 = img.crop(img4_box)
img1.save("1.jpg")
img2.save("2.jpg")
img3.save("3.jpg")
img4.save("4.jpg")
