#! /usr/bin/python
#! -*- coding:utf-8 -*-

# wxpy微信接口模块的学习文件

from wxpy import *
import os

# qrcode的回调函数，如果无此函数，qrcode将不会存储到本地
def qc(uuid,status,qrcode):
    print('Ok!qrcode had downloaded!')
    return

# 实例化一个机器人
bot = Bot(cache_path=True,console_qr=2,qr_callback=qc)

# 消息的发送
# 找好友，获取一个消息对象
my_friend = bot.friends().search('Ly',sex=MALE,city='石家庄')[0]
my_friend.send('Hi,boy')