from PIL import Image
import os, sys
if(len(sys.argv) < 3):
	print("用法：convert 原图像文件名 目标图像文件名")
	sys.exit(0)
src_file = sys.argv[1]
dest_file = sys.argv[2]

try:
	with Image.open(src_file) as img:
		img.save(dest_file)
		print("转换成功！")
except OSError:
	print("不能转换文件：", src_file)

