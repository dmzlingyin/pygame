#! /usr/bin/python
#! -*- coding:utf-8 -*-
# 微信图灵机器人
# Date:2019-04-20

import itchat
import requests
import time
import os
import threading


# 图灵服务器ｋｅｙ
KEY='a172a26eb1534616a7762b4568d0893d'

# 第一次请求对话
FIRST = True

import itchat, time, sys

def output_info(msg):
    print('[INFO] %s' % msg)

def open_QR():
    for get_count in range(10):
        output_info('Getting uuid')
        uuid = itchat.get_QRuuid()
        while uuid is None: uuid = itchat.get_QRuuid();time.sleep(1)
        output_info('Getting QR Code')
        if itchat.get_QR(uuid=uuid): break
     
        elif get_count >= 9:
            output_info('Failed to get QR Code, please restart the program')
            sys.exit()
    output_info('Please scan the QR Code')
    return uuid

uuid = open_QR()
os.popen('python3 fi_mail.py')

waitForConfirm = False
while 1:
    status = itchat.check_login(uuid)
    if status == '200':
        break
    elif status == '201':
        if waitForConfirm:
            output_info('Please press confirm')
            waitForConfirm = True
    elif status == '408':
        output_info('Reloading QR Code')
        uuid = open_QR()
        waitForConfirm = False
userInfo = itchat.web_init()
itchat.show_mobile_login()
itchat.get_friends(True)
output_info('Login successfully')
itchat.start_receiving()



# # 微信登出后的回调函数
def ec():
  
    itchat.send('微信已登出','filehelper')

# 图灵服务器交互函数
def get_msg_from_tuling(msg):
    ApiUrl = 'http://www.tuling123.com/openapi/api'

    #向图灵发送的消息
    data = {
        'key':KEY,
        'info':msg,
        'userid':'dmzlingyin'
    }


    # 第一次请求对话时，返回提示信息
    global FIRST
    if FIRST:
        FIRST = False
        return "你好,机器人v1.0，工作时间　08：00--22：00，如有急事，请拨打电话：15033685022，如无急事，和我聊天也是可以的哦！"


    # 进行发送
    try:
        r = requests.post(ApiUrl,data=data).json()

        return r.get('text')

    except:
        return None



# 消息注册
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):

    localtime = time.localtime(time.time())
    if localtime[3] >= 22:
        itchat.logout()

    # 如果图灵服务器出现问题，会回复原话
    defaultReply = 'I received:' + msg['Text']

    reply = get_msg_from_tuling(msg['Text']) + '\n' + '－robot'
    return reply or defaultReply



# 运行
itchat.run()
