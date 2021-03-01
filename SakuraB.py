#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: jiangyongling
# datetime: 1/2/2021 下午1:21
# file : SakuraB.py
# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 7:40 下午
# @Author  : SunRuichuan
# @File    : damo_percent.py
import requests
import grequests


user_url = 'http://m.qa2.inagora.org/user/'
login_url = 'http://m.qa2.inagora.org/user/ajaxLoginBySms'
pick_damo = 'http://m.qa2.inagora.org/sakura/ajaxUserOpenSakuraReward'
get_damo = 'http://m.qa2.inagora.org/sakura/ajaxUserLotterySakura'
visit_damo = 'http://m.qa2.inagora.org/sakura/index'
merge_damo = 'http://m.qa2.inagora.org/sakura/ajaxUserComposeSakura'


def get_crsf_token():
    res = requests.get(url=user_url)
    data = {
        "Csrf-Token-fe1a2a3s12": res.cookies.get("Csrf-Token-fe1a2a3s12"),
        "Wonderfull-Session-Id": res.cookies.get("Wonderfull-Session-Id"),
        "user_key": res.cookies.get("user_key")
    }
    return data


def get_token_by_sms(phone, _cookies):
    headers = {
        "Csrf-Token-fe1a2a3s12": _cookies["Csrf-Token-fe1a2a3s12"],
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "34",
        "Content-Type": "application/x-www-form-urlencoded",
        # "Csrf-Token-fe1a2a3s12": "7a9126ef987199c4326584bc829b6cb810144932",
        "Host": "m.qa2.inagora.org",
        "Origin": "http://m.qa1.inagora.org",
        "Pragma": "no-cache",
        "Referer": "http://m.qa1.inagora.org/user/login",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
        "verify_code": 7431
    }
    res = requests.post(url=login_url, data=data, cookies=_cookies, headers=headers)
    if res.json()['errno'] == 0:
        return res.json()['data']['info']['token']
    else:
        return ""


def get_coupon(_token, _cookies):
    headers = {
        "Csrf-Token-fe1a2a3s12": _cookies["Csrf-Token-fe1a2a3s12"],
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        "content-length": "0",
        # "csrf-token-fe1a2a3s12": "be258db8333a734521808a536d1db264621e74e4",
        "origin": "http://m.qa1.inagora.org",
        "referer": "http://m.qa1.inagora.org/activity/main20201212",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "x-requested-with": "XMLHttpRequest",
    }
    _cookies.update({"token": _token})
    res = requests.post(url=pick_damo, cookies=_cookies, headers=headers)
    print(res.text)


def pick_honghao(count):
    tokens = []
    cookies = []
    aa = bb = cc = dd = 0.00
    # for i in range(0, count):
    cookie = get_crsf_token()
    token = get_token_by_sms(14422441008, cookie)
    tokens.append(token)
    cookies.append(cookie)
    # print(str(i) + "%")

    # print(tokens)
    task = []
    for i in range(0, 20):
        damo_cookie = cookies[0]
        damo_token = tokens[0]
        damo_headers = {
            "Csrf-Token-fe1a2a3s12": damo_cookie["Csrf-Token-fe1a2a3s12"],
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
            "content-length": "0",
            # "csrf-token-fe1a2a3s12": "be258db8333a734521808a536d1db264621e74e4",
            "origin": "http://m.qa1.inagora.org",
            "referer": "http://m.qa1.inagora.org/activity/main20201212",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "x-requested-with": "XMLHttpRequest",
        }
        damo_cookie.update({"token": damo_token})
        req = grequests.request("POST", pick_damo, headers=damo_headers, cookies=damo_cookie)
        task.append(req)

    resp = grequests.map(task)
    for j in resp:
        print(j.json())
        # cash = float(j.json()['data']['cash_amount'])
        # if cash == 100.00:
        #     aa = aa + 1
        # elif 40.00 < cash < 60.00:
        #     bb = bb + 1
        # elif 15.00 < cash < 20.00:
        #     cc = cc + 1
        # elif 8.00 < cash < 2.00:
        #     dd = dd + 1

    # total = aa + bb + cc + dd
    # print(aa, bb, cc, dd)
    # print(aa/total, bb/total, cc/total, dd/total)


def pick_damo_per(count):
    tokens = []
    cookies = []
    a = b = c = d = e = 0
    # for i in range(0, count):
    cookie = get_crsf_token()
    token = get_token_by_sms(14422441008, cookie)
    tokens.append(token)
    cookies.append(cookie)
    # print(str(i) + "%")

    print(tokens)
    task = []
    for i in range(0, 20):
        coupon_cookie = cookies[0]
        coupon_token = tokens[0]
        refresh_damo(coupon_cookie, coupon_token)
        coupon_headers = {
            "Csrf-Token-fe1a2a3s12": coupon_cookie["Csrf-Token-fe1a2a3s12"],
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
            "content-length": "0",
            # "csrf-token-fe1a2a3s12": "be258db8333a734521808a536d1db264621e74e4",
            "origin": "http://m.qa1.inagora.org",
            "referer": "http://m.qa1.inagora.org/activity/main20201212",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "x-requested-with": "XMLHttpRequest",
        }
        coupon_cookie.update({"token": coupon_token})
        req = grequests.request("POST", get_damo, headers=coupon_headers, cookies=coupon_cookie)
        task.append(req)

    resp = grequests.map(task)
    for j in resp:
        if j.json()['errno'] == 0:
            damo = j.json()['data']['sakura_key']
            cat = damo.split('_')[1]
            if cat == "a":
                a = a + 1
            elif cat == "b":
                b = b + 1
            elif cat == "c":
                c = c + 1
            elif cat == "d":
                d = d + 1
            elif cat == "e":
                e = e + 1
    total = a + b + c + d + e
    print(a, b, c, d, e)
    print(a/total, b/total, c/total, d/total, e/total)


def refresh_damo(_cookie, _token):
    coupon_headers = {
        "Csrf-Token-fe1a2a3s12": _cookie["Csrf-Token-fe1a2a3s12"],
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        "content-length": "0",
        # "csrf-token-fe1a2a3s12": "be258db8333a734521808a536d1db264621e74e4",
        "origin": "http://m.qa1.inagora.org",
        "referer": "http://m.qa1.inagora.org/activity/main20201212",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "x-requested-with": "XMLHttpRequest",
    }
    _cookie.update({"token": _token})
    requests.get(url=visit_damo, headers=coupon_headers, cookies=_cookie)
    # print(res)


def merge_damo():
    tokens = []
    cookies = []
    cookie = get_crsf_token()
    token = get_token_by_sms(14422220001, cookie)
    tokens.append(token)
    cookies.append(cookie)

    print(tokens)
    print(cookies)
    task = []
    for i in range(0, 20):
        merge_cookie = cookies[0]
        merge_token = tokens[0]
        # refresh_damo(coupon_cookie, coupon_token)
        merge_headers = {
            "Csrf-Token-fe1a2a3s12": merge_cookie["Csrf-Token-fe1a2a3s12"],
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
            "content-length": "0",
            # "csrf-token-fe1a2a3s12": "be258db8333a734521808a536d1db264621e74e4",
            "origin": "http://m.qa1.inagora.org",
            "referer": "http://m.qa1.inagora.org/sakura/",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "x-requested-with": "XMLHttpRequest",
        }
        merge_cookie.update({"token": merge_token})
        req = grequests.request("POST", url=merge_damo, headers=merge_headers, cookies=merge_cookie)
        task.append(req)

    resp = grequests.map(task)
    print(resp)
    for j in resp:
        print(j.json())


if __name__ == '__main__':
    pick_damo_per(10)
    #merge_damo()
    # pick_honghao(1)

