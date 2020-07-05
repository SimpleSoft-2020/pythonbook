from PIL import Image
import os, sys
if(len(sys.argv) < 3):
	print("用法：convert 原图像文件名 目标图像文件名")
	sys.exit(0)
src_file = sys.argv[1]
dest_file = sys.argv[2]
#缩略图大小
thumbnail_size = (64, 64)

try:
	with Image.open(src_file) as img:
		img.thumbnail(thumbnail_size)
		img.save(dest_file)
		print("保存缩略图成功！")
except OSError:
	print("不能打开文件：", src_file)

