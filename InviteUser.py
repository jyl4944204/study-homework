#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: jiangyongling
# datetime: 30/1/2021 下午7:26
# file : InviteUser.py
import faker

from API.APP.h5.LoginH5 import loginBySms
f = faker.Faker(locale='zh-CN')

print(f.ssn())
ch = "hd_wd_sys_xiaoniu2021"
invite_id = '1379970'
res = loginBySms('qa1', '14499999118', 7431,ch,invite_id)
print(res.json())

