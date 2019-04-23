#! /usr/bin/python
#! -*- coding:utf-8 -*-
# 微信图灵机器人
# Date:2019-04-20

import itchat
import requests
import time
import os



# 图灵服务器ｋｅｙ
KEY='a172a26eb1534616a7762b4568d0893d'

# 第一次请求对话
FIRST = True

# def send_mail():
#     os.popen('python3 fj_mail.py')

# T = threading.Thread(target=send_mail)


# 登录成功后的回调函数
# def qc(uuid,status,qrcode):
#     itchat.get_QR()
#     os.popen('python3 fj_mail.py')
#     itchat.send('你的微信在wed端登录！','filehelper')
    



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
# 登录


itchat.auto_login(hotReload=True)




# 运行
itchat.run()
