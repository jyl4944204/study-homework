#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: jiangyongling
# datetime: 31/1/2021 下午4:34
# file : contact.py
class Contact:
    def __init__(self):
        self.corpid = ""
        self.corpsecret = ""

    def get_token(self,corpid=None,corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        pass
    def delete_member(self):
        pass
    def update_member(self):
        pass
    def create_member(self):
        pass
    def select_member(self):
        pass