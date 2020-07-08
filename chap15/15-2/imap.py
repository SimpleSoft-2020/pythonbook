import imaplib
import sys

# 邮件服务器
imap_server = 'imap.qq.com'
#用户名授权码
#记住要改成自己的用户名
user_name = '3405187170@qq.com'
#授权码，不是密码，换成自己的授权码
auth_code = 'yhqjoy****elrdbji'
imap = imaplib.IMAP4_SSL(imap_server)
#进行身份认证
imap.login(user_name,auth_code)
#选择收件箱
imap.select()
res,data = imap.search(None,'ALL')
#获取所有邮件编号
mails=data[0].split()
#获取第一封邮件
typ, mail_content = imap.fetch(mails[0], '(RFC822)')
#打印邮件内容
print(mail_content)
imap.close()
imap.logout()


