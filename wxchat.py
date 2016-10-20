# -*-coding:utf-8 -*-
import itchat
from itchat.content import *
import requests as rs
import json
import _thread
import time

def auto_msg(txt):
	url = 'http://www.niurenqushi.com/api/simsimi/'
	header = {'Host':'www.niurenqushi.com','Origin':'http://www.niurenqushi.com'
          ,'Referer':'http://www.niurenqushi.com/app/simsimi/'
          ,'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
         }
	data = {'txt':txt}

	t = rs.post(url,data=data,headers=header)
	return json.loads(t.text)['text'].replace('图灵机器人','阿远私人助手').replace('硕硕','')


temp_name = {'name':''}
online = 0
talk = 0

print('runing model:%s'%online)
# @itchat.msg_register(TEXT, isGroupChat = True)
# def text_reply(msg):
#     print(msg['isAt'])
#     print(msg['ActualNickName'])
#     print(msg['Content'])
#     print(msg['Text'])


@itchat.msg_register(['Text','Picture','Recording'])
def text_reply(msg):
	print('From',msg['Content'])
	global online,talk
	if '开启自动回复' in msg['Text']:

		online = 1
		itchat.send('自动回复已开启')

	elif '关闭自动回复' in msg['Text']:
		online = 0
		itchat.send('自动回复已关闭')

	if online and '开启自动回复' not in msg['Text']:
		if talk == 0:
			if '小i' in msg['Text']:
				itchat.send('哈喽，我就是上知天文下知地理，前知5000年，后知800年的小i，你想知道啥尽管放马过来～哈哈哈',msg['FromUserName'])
				talk = 1			
			else:
				itchat.send('你好，主人不在，我是他的智能助手小i，啥事请留言，或者回复“小i”，跟我聊聊人生～～',msg['FromUserName'])
		else:
			if '退出小i' in msg['Text']:
				talk = 0
			else:
				
				print('From',msg['Content'])
				temp_name['name'] = msg['FromUserName']
				itchat.send(msg['Content'],'ms-xiaoice')
	else:
		pass
	# print(msg['Text'],'6')
	# print(msg['ToUserName'],'2')
	# print(msg['FromUserName'],'5')
	# print('from~%s'%msg['Text'])
	# txt = auto_msg(msg['Text'])
	# print(msg['Text'])
	# itchat.send(txt, msg['FromUserName'])
	# print(msg['Text'])


@itchat.msg_register(['Text','Picture','Recording'],isMpChat=True)
def text_reply(msg):
    # itchat.send(msg['Text'], msg['FromUserName'])
    # itchat.send('注意以下发言为自动回复', msg['FromUserName'])
	# print(msg['Content'],'3')
	# print(msg['ToUserName'],'3')
	# print(msg['FromUserName'],'6')
	# print(temp_name['name'],'7')
	print('To',msg['Text'])
	itchat.send(msg['Content'],temp_name['name'])
	temp_name['name'] = ''



	# if msg['ToUserName'] == 'ms-xiaoice': 
	# 	pass
	# else:
		# print('from~%s'%msg['Text'])
	# txt = auto_msg(msg['Text'])
		# itchat.send(msg['Text'],'ms-xiaoice')
		# print(msg['Text'])

	# itchat.send(txt, msg['FromUserName'])
	# print(msg['Text'])

@itchat.msg_register(['Text','Picture','Recording'],isGroupChat = True)
def text_reply(msg):
    # itchat.send(msg['Text'], msg['FromUserName'])
    # itchat.send('注意以下发言为自动回复', msg['FromUserName'])
	global online
	if online:
		if msg['isAt']:
			print(msg['Text'])
			temp_name['name'] = msg['FromUserName']
			itchat.send(msg['Content'],'ms-xiaoice')
	else:
		pass

    	# txt = auto_msg(msg['Text'])
    	# print(txt)
    	# itchat.send(txt, msg['FromUserName'])
# 在注册时增加isGroupChat=True将判定为群聊回复
# @itchat.msg_register(itchat.content.TEXT, isGroupChat = True)
# def groupchat_reply(msg):
#     # if msg['isAt']:
#         txt = auto_msg(msg['Text'])
#         # itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], txt), msg['FromUserName'])
#         itchat.send(txt, msg['FromUserName'])
#         # msg['Content']

itchat.auto_login(True)

_thread.start_new_thread(itchat.run())
while 1:
	itchat.configured_reply()
	time.sleep(0.1)