import itchat

itchat.auto_login(hotReload=True)

# friends为一个列表，列表元素为字典
# 使用update将e等新好友列表，并返回
friends = itchat.get_friends(update=True)

# 好友总个数
num_friend = len(friends) - 1

# 男性好友个数
M = 0

# 女性好友个数
W = 0
with open('friend.txt','w+') as f:
    # for friend in friends[1:]:
    #     print(friend['RemarkName'])
    #     if friend['Sex'] == 1:
    #         print('性别男')
    #         M = M + 1
    #     else:
    #         print('性别女')
    #         W = W + 1
    #     print(friend.get('Signature'))
    #     print(friend['Province']+friend['City'])
    for friend in friends[1:]:
        f.write(friend['RemarkName'])
        f.write('\t')
        if friend['Sex'] == 1:
            f.write('性别男')
            M = M + 1
        else:
            f.write('性别女')
            W = W + 1
        
        f.write('\t')
        f.write(friend.get('Signature'))
        f.write('\t')
        f.write(friend['Province']+friend['City'])
        f.write('\n')
        f.write('\n')



print('你共有%d个微信好友' % num_friend)
print('女性好友:%d个' % W)
print('男性好友:%d个' % M)


# 公众号的获取
mps = itchat.get_mps(update=True)
num_mp = len(mps)
for mp in mps:
    print(mp['NickName'])

print('你一共关注了%d个公众号' % num_mp)

# 群聊 获取
chatrooms = itchat.get_chatrooms(update=True)
num_chatroom = len(chatrooms)

for chatroom in chatrooms:
    print(chatroom['NickName'])


print('你一共加入了%d个群聊' % num_chatroom)
itchat.run()


# 需要获取好友的:
# RemarkName
# Sex
# Signature
# Province
# City



# 公众号的格式:
# {   'MemberList': <ContactList: []>, 
#     'Uin': 0, 
#     'UserName': '@3cd0d8c4e80539fb956e98a7bb2b9f23', 
#     'NickName': '河北共青团', 
#     'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=661064658&username=@3cd0d8c4e80539fb956e98a7bb2b9f23&skey=@crypt_1685a326_e1006924e61269ef2d57207374fabb23', 
#     'ContactFlag': 3, 
#     'MemberCount': 0, 
#     'RemarkName': '',
#     'HideInputBarFlag': 0, 
#     'Sex': 0, 'Signature':
#     '服务广大青年，展示冀青风采！', 
#     'VerifyFlag': 24, 
#     'OwnerUin': 0, 
#     'PYInitial': 'HBGQT', 
#     'PYQuanPin': 'hebeigongqingtuan', 
#     'RemarkPYInitial': '', 
#     'RemarkPYQuanPin': '', 
#     'StarFriend': 0, 
#     'AppAccountFlag': 0, 
#     'Statues': 0,
#     'AttrStatus': 0, 
#     'Province': '河北', 
#     'City': '石家庄', 
#     'Alias': '', 
#     'SnsFlag': 0, 
#     'UniFriend': 0, 
#     'DisplayName': '',
#     'ChatRoomId': 0,
#     'KeyWord': 'gh_', 
#     'EncryChatRoomId': '', 
#     'IsOwner': 0
# }


# 群聊的格式:
# {
#     'MemberList': <ContactList: []>, 
#     'Uin': 0, 
#     'UserName': '@@eeac2276a9ed41c00f0ffc2063e1c81200f794a6226eb450f0a3ace6247e19b1', 
#     'NickName': '你懂的', 
#     'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgetheadimg?seq=661058395&username=@@eeac2276a9ed41c00f0ffc2063e1c81200f794a6226eb450f0a3ace6247e19b1&skey=@crypt_1685a326_e1006924e61269ef2d57207374fabb23', 
#     'ContactFlag': 1, 
#     'MemberCount': 0, 
#     'RemarkName': '', 
#     'HideInputBarFlag': 0, 
#     'Sex': 0, 
#     'Signature': '', 
#     'VerifyFlag': 0, 
#     'OwnerUin': 0,
#     'PYInitial': 'NDD', 
#     'PYQuanPin': 'nidongde', 
#     'RemarkPYInitial': '',
#     'RemarkPYQuanPin': '', 
#     'StarFriend': 0, 
#     'AppAccountFlag': 0, 
#     'Statues': 1, 
#     'AttrStatus': 0, 
#     'Province': '', 
#     'City': '', 
#     'Alias': '', 
#     'SnsFlag': 0, 
#     'UniFriend': 0, 
#     'DisplayName': '',
#     'ChatRoomId': 0, 
#     'KeyWord': '',
#     'EncryChatRoomId': '',
#     'IsOwner': 0,
#     'IsAdmin': None, 
#     'Self': <User: {'MemberList': <ContactList: []>,
#                 'UserName': '@c610bc0496be639b667f3bd40027f440611b4c47986499e9552aac9b1af7c156', 
#                 'City': '', 
#                 'DisplayName': '', 
#                 'PYQuanPin': '', 
#                 'RemarkPYInitial': '', 
#                 'Province': '', 
#                 'KeyWord': '', 
#                 'RemarkName': '', 
#                 'PYInitial': '', 
#                 'EncryChatRoomId': '', 
#                 'Alias': '', 
#                 'Signature': '知识可以速成，阅历却不能恶补。',
#                 'NickName': 'GhoulLingyin', 
#                 'RemarkPYQuanPin': '', 
#                 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=1817820153&username=@c610bc0496be639b667f3bd40027f440611b4c47986499e9552aac9b1af7c156&skey=@crypt_1685a326_e1006924e61269ef2d57207374fabb23', 
#                 'UniFriend': 0, 
#                 'Sex': 1, 
#                 'AppAccountFlag': 0, 
#                 'VerifyFlag': 0, 
#                 'ChatRoomId': 0,
#                 'HideInputBarFlag': 0, 
#                 'AttrStatus': 0, 
#                 'SnsFlag': 1, 
#                 'MemberCount': 0, 
#                 'OwnerUin': 0, 
#                 'ContactFlag': 0, 
#                 'Uin': 372771080, 
#                 'StarFriend': 0,
#                 'Statues': 0, 
#                 'WebWxPluginSwitch': 0,
#                 'HeadImgFlag': 1}>
       
# }