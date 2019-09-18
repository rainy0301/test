
# -*- coding: utf-8 -*-
'''
author: Levi
version: 1.0
date: 2019-09-18
description: 企业微信机器人信息函数, 支持文字，图片，markdown文本
'''

from requests import Session
import base64
import hashlib


def get_md5_value(str):
        my_md5 = hashlib.md5()#获取一个MD5的加密算法对象
        my_md5.update(str) #得到MD5消息摘要
        hash = my_md5.hexdigest()#以16进制返回消息摘要，32位
        return hash


def send_message(url,content,types):
    '''
    url: 企业微信机器人消息接收地址;
    content: 文本内容；types为figure时，是图片的文件名字(含扩展名);
    types: 消息类型，text：文本；markdown：markdown文本; figure: 图片
    '''
    s = Session()
    if types == 'text':
        data = {
                "msgtype": "text",
                "text": {
                    "content": content,
                    "mentioned_list":["@all"]                    
                    }
                }
    elif types == 'markdown':
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": content,
                "mentioned_list":["@all"]
            }
        }
    elif types == 'figure':
        with open("%s"%content,"rb") as f:#转为二进制格式
            ff = f.read()
            md5 = get_md5_value(ff)
            base64_data = base64.b64encode(ff)#使用base64进行加密
        data = {
                "msgtype": "image",
                "image": {
                    "base64": base64_data,
                    "md5": md5
                    }
                }

    headers = {"Content-Type": "text/plain"}
    p = s.post(url,headers=headers,json=data)
    if p.status_code==200:
        print('发送成功')
    else:
        print(p.text)

if __name__ == "__main__":
    url = '企业微信机器人Webhook地址'
    content = '你好，我是企业微信小机器人'
    send_message(url,content,'text')
