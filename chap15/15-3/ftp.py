import ftplib

ftp = ftplib.FTP()
#换成自己的ftp地址和端口号
ftp.connect('10.0.0.3',3721)
#匿名登录
ftp.login()
#查看ftp服务器当前目录下的文件
ftp.dir()
#下载文件
#以写模式在本地打开文件
filename = "20200708.txt"
file=open(filename,'wb').write 
#从服务器获取文件并写入本地文件
ftp.retrbinary('RETR '+ filename,file)
print("下载文件成功")
#上传文件到服务器
fp=open(filename,'rb')
ftp.storbinary('STOR ' +filename,fp)
print("上传文件成功")
fp.close()
ftp.quit()

