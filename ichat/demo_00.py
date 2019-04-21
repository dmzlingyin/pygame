# itchat学习Ｄemo
# Author:Lingyin
# Date:2019-04-20
# Reference:https://itchat.readthedocs.io/zh/latest/tutorial/tutorial0/

import itchat

# ----------------------------------------------------------------------
# 微信消息获取
# 通过装饰器将print_contenti注册处文消息函数
# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg['Text'])
# ----------------------------------------------------------------------

# **********************************************************************
# 微信登录
# 多次运行程序只扫一次，hotReload=True
# 命令行二维码:enableCmdQR=Ｔrue(linux系统的字符宽度，设置为：enableCmdQR=2)
# itchat.auto_login(hotReload=True,enableCmdQR=2)

# #开始运行
# itchat.run()

itchat.auto_login(hotReload=True)


# 微信消息发送
# 发送自定义的消息

# itchat.send('Hello Lingyin','filehelper')

# 在注册函数中直接回复
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return msg['Text']

itchat.run()
