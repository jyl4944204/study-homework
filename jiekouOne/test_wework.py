#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: jiangyongling
# datetime: 28/1/2021 下午9:40
# file : test_wework.py
import requests


def get_token():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2e93dda868258303&corpsecret=wV8d2jzFRfTw0txKNL1vwg3eQnOtauiXFDhZ2JjxZmM"
    res = requests.get(url)
    print(res.json())
    token = res.json()['access_token']
    return token

def test_update_member():
    token = get_token()
    print(token)
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    print(url)
    data = {
        "userid": "chengrui1",
        "name": "李四"
    }
    res = requests.post(url,json=data)
    print(res.json())