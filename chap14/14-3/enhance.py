from PIL import Image
from PIL import ImageEnhance

img = Image.open("test.jpg")
enhance = ImageEnhance.Contrast(img)
#对比度增加为1.5倍
enhance.enhance(1.5).show("对比度")
#亮度增加为1.5倍
enhance = ImageEnhance.Brightness(img)
enhance.enhance(1.5).show("亮度")
#锐化
enhance = ImageEnhance.Sharpness(img)
enhance.enhance(1.5).show("锐化")
#模糊
enhance = ImageEnhance.Sharpness(img)
enhance.enhance(0).show("模糊")
#颜色变化
enhance = ImageEnhance.Color(img)
enhance.enhance(0).show("黑白")
#颜色变化
enhance = ImageEnhance.Color(img)
enhance.enhance(1.5).show("颜色加深")
