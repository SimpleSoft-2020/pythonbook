import urllib.request
import shutil
import sys

if(len(sys.argv) < 3):
	print("请输入网址和要保存的文件名")
	print("python geturl.py <url> <file name>")
	sys.exit()

url = sys.argv[1]
file_name = sys.argv[2]
#打开URL
with urllib.request.urlopen(url) as response:
	#打开文件
	with open(file_name,'wb') as file:
		#将response的内容写入到文件中
		shutil.copyfileobj(response,file)


