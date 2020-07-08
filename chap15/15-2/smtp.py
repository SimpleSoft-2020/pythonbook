import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import sys

#邮件发送者
msg_from='3405187170@qq.com'
#授权码，改成自己的真实的授权码
auth_code='****'
#收件者，为一个列表，可以发给多个人
msg_to=['3405187170@qq.com',]

#获取https://www.python.org/网页作为邮件的内容
result = requests.get('https://www.python.org')
content=result.content
#邮件标题
subject="测试邮件"
#构建邮件消息
#支持html以及附件
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = ", ".join(msg_to)
msg.attach(MIMEText(content,_subtype='html',_charset='UTF-8'))

#添加一个附件，test.zip
att = MIMEText(open('test.zip','rb').read(), 'base64', 'gb2312')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="test.zip"'
msg.attach(att)

smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
smtp.login(msg_from, auth_code)
smtp.sendmail(msg_from, msg_to, msg.as_string())
smtp.quit()
print ("发送邮件成功")
