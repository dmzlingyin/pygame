import itchat, time, sys

def output_info(msg):
    print('[INFO] %s' % msg)

# def open_QR():
#     for get_count in range(10):
#         output_info('Getting uuid')
#         uuid = itchat.get_QRuuid()
#         while uuid is None: uuid = itchat.get_QRuuid();time.sleep(1)
#         output_info('Getting QR Code')
#         if itchat.get_QR(uuid): break
#         elif get_count >= 9:
#             output_info('Failed to get QR Code, please restart the program')
#             sys.exit()
#     output_info('Please scan the QR Code')
#     return

# # uuid = 
# open_QR()
uuid = itchat.get_QRuuid()
itchat.get_QR(uuid,picDir="./test.png")
# waitForConfirm = False
# while 1:
#     status = itchat.check_login(uuid)
#     if status == '200':
#         break
#     elif status == '201':
#         if waitForConfirm:
#             output_info('Please press confirm')
#             waitForConfirm = True
#     elif status == '408':
#         output_info('Reloading QR Code')
#         uuid = open_QR()
#         waitForConfirm = False
# userInfo = itchat.web_init()
# itchat.show_mobile_login()
# itchat.get_friends(True)
# output_info('Login successfully')
# itchat.start_receiving()

# Start auto-replying
@itchat.msg_register
def simple_reply(msg):
    if msg['Type'] == 'Text':
        return 'I received: %s' % msg['Content']
itchat.run()