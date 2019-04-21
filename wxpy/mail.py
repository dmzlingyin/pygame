# from email.mime.text import MIMEText
# import smtplib
# from email.header import Header

# msg = MIMEText('smtp server','plain','utf-8')
# msg['Subject'] = Header('this is a python mail','utf-8')

# from_addr = 'dmzlingyin@163.com'
# password = 'lingyin123'
# to_addr = '2686291180@qq.com'

# server = smtplib.SMTP('smtp.163.com',25)
# server.set_debuglevel(1)
# server.login(from_addr,password)

# server.sendmail(from_addr,[to_addr,'dmzlingyin@163.com'],msg.as_string())

# server.quit()

# from email.mime.text import MIMEText
#
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# # 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
# # 输入收件人地址:
# to_addr = input('To: ')
#
# import smtplib
#
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()




# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'dmzlingyin@163.com'
receiver = '2686291180@qq.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'dmzlingyin@163.com'
password = 'lingyin123'  # 是授权密码，而不是登录密码

msg = MIMEText('你好', 'text', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'dmzlingyin@163.com'
msg['To'] = '2686291180@qq.com'

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()