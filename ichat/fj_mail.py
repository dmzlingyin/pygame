#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender = '2686291180@qq.com'
receivers = ['dmzlingyin@163.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_host="smtp.qq.com" #设置服务器
mail_user="2686291180@qq.com" #用户名
mail_pass="bcxyskdfedwpdeia" #口令
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("微信web-Pi", 'utf-8')
message['To'] = Header("登录", 'utf-8')
subject = '登录确认'
message['Subject'] = Header(subject, 'utf-8')
#邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('QR.png', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="QR.png"'
message.attach(att1)
# # 构造附件2，传送当前目录下的 runoob.txt 文件
# att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
# message.attach(att2)

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25) # 25 为 SMTP 端口号
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")