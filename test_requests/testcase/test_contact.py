#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: jiangyongling
# datetime: 31/1/2021 下午4:37
# file : test_contact.py
from test_requests.req_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()

