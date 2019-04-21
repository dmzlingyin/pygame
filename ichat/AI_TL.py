#! /usr/bin/python
#! coding:utf-8
# 微信图灵机器人
# Date:2019-04-20

import itchat
import requests
import time

# 图灵服务器ｋｅｙ
KEY='a172a26eb1534616a7762b4568d0893d'

# 第一次请求对话
FIRST = True



# 图机器服务器交方法
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

    reply = get_msg_from_tuling(msg['Text']) + '\n' + '__robot__'
    return reply or defaultReply
# 登录
itchat.auto_login(hotReload=True,enableCmdQR=2,picDir='/home/lingyin/test.png')

# 运行
itchat.run()
