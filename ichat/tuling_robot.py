#! /usr/bin/python
#! coding:utf-8
# 图灵机器人测试
import itchat
import requests

ApiUrl = 'http://www.tuling123.com/openapi/api'

# 发送规则:json格式

data = {
    'key':'1107d5601866433dba9599fac1bc0083',
    'info':'我想看新闻',
    'userid':'wechat_robot',
}

# 通过post发送
r = requests.post(ApiUrl,data=data).json()
print(r['text'])
for article in r['list']:
    print(article['article'] + '\t' + article['source'])
