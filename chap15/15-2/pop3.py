import poplib
import sys

# 邮件服务器
pop3_server = 'pop.qq.com'
#用户名授权码
#记住要改成自己的用户名
user_name = '3405187170@qq.com'
#授权码，不是密码，换成自己的授权码
auth_code = 'yhqjoy****elrdbji'
pop3 = poplib.POP3_SSL(pop3_server)
#设置调试模式
pop3.set_debuglevel(1)
#获取欢迎信息
pop3.getwelcome()
#进行身份认证
pop3.user(user_name)
pop3.pass_(auth_code)
unread_mail,total_size = pop3.stat()
response,mails,octets = pop3.list()
if(len(mails) < 1):
	print("没有邮件")
	pop3.quit()
	sys.exit(0)

#获取第一封邮件
mail = pop3.retr(1)
#打印邮件内容
print(mail)
pop3.quit()

