#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: jiangyongling
# datetime: 31/1/2021 上午10:18
# file : OpenMoney.p
import random

import requests
from requests import Session

from API.APP.h5.LoginH5 import getTokenByPassword, getCrsfToken, loginByPassword

class OpenMoney:

    #开红包
    def userOpenSakuraReward(self,qa):
        _cookies = getCrsfToken(qa)
        res = getTokenByPassword(qa,'15010216358','jyl4944204')
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
        _cookies.update({"token": res})
        url = "http://m.qa1.inagora.org/sakura/ajaxUserOpenSakuraReward"
        sum1 = 0 # cash1
        sum2 = 0 # cash2
        sum3 = 0 # cash3
        sum4 = 0 # 优惠券1
        sum5 = 0 # 优惠券2
        sum6 = 0 # 0元购
        sum7 = 0 # 积分
        sumzong = 0
        cash = 0

        for i in range(100):
            sumzong = sumzong + 1

            res1 = requests.post(url=url, cookies=_cookies, headers=headers).json()
            #res1={'errno': 0, 'errmsg': 'ok', 'data': {'id': '1623', 'type': '1', 'status': '0', 'cash': '0.96', 'score': '144', 'score_exchange_money': '2.88', 'coupon_price': 0, 'coupon_desc1': '豌豆公主App全场通用', 'coupon_desc2': '', 'goods_price': 0, 'goods_img': '', 'goods_name': '', 'goods_desc': '', 'ctime': '2021-02-01 18:00:46'}}


            type = res1['data']['type']
            cash = res1['data']['cash']
            coupon_price = res1['data']['coupon_price']
            if type == '1':
                print(type)
                if 0.3 <= float(cash) <= 2:
                    sum1 = sum1 + 1
                if 20 <= float(cash) <= 40:
                    sum2 = sum2 + 1
                if float(cash) == 100:
                    sum3 = sum3 + 1
            # 优惠券
            elif type == '2':
                if int(coupon_price) == 5:
                    sum4 = sum4 + 1
                if int(coupon_price) == 10:
                    sum5 = sum5 + 1

            # 0元购
            elif type == '4':
                sum6 = sum6 + 1

            # 积分
            elif type == '5':
                sum7 = sum7 + 1
        print(sum1)
        print(sum2)
        print(sum3)
        print(sum4)
        print(sum5)
        print(sum6)
        print(sum7)

        print("sumzong的值为：" + str(sumzong))
        print("现金1sum1的值为：" + str(sum1/sumzong))
        print("现金2sum2的值为：" + str(sum2/sumzong))
        print("现金3sum3的值为：" + str(sum3/sumzong))
        print("优惠券1sum4的值为：" + str(sum4/sumzong))
        print("优惠券2sum5的值为：" + str(sum5/sumzong))
        print("0元购sum6的值为：" + str(sum6/sumzong))
        print("积分sum7的值为：" + str(sum7/sumzong))

    def hecheng(self,qa):
        url = "http://m.qa1.inagora.org/sakura/ajaxUserComposeSakura"
        _cookies = getCrsfToken(qa)
        res = getTokenByPassword(qa, '15010216358', 'jyl4944204')
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
        _cookies.update({"token": res})
        for i in range(200):
            res = requests.post(url=url, cookies=_cookies, headers=headers).json()
            print(url)
            print(res)
            # res.content.decode("utf-8")
            # if res['errno'] == '0':
            print("第" + str(i) + "次")

    # 抽字卡
    def userLotterySakura(self,qa):
        url = "http://m.qa1.inagora.org/sakura/ajaxUserLotterySakura"
        _cookies = getCrsfToken(qa)
        res = getTokenByPassword(qa, '15010216358', 'jyl4944204')
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
        _cookies.update({"token": res})
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        w = 0
        Z = 0

        for i in range(200):
            res = requests.post(url=url, cookies=_cookies, headers=headers).json()

            print(url)
            print(res)
            #res.content.decode("utf-8")
            #if res['errno'] == '0':
            print("第" + str(i) +"次")
            Z = Z + 1
            if res['data']['sakura_key'] == "sakura_a":
                a = a+1
            elif res['data']['sakura_key'] == "sakura_b":
                b = b + 1
            elif res['data']['sakura_key'] == "sakura_c":
                c = c + 1
            elif res['data']['sakura_key'] == "sakura_d":
                d = d + 1
            elif res['data']['sakura_key'] == "sakura_e":
                e = e + 1
            elif res['data']['sakura_key'] == "sakura_w":
                w = w + 1
        print("a的值为：" + str(a/Z))
        print("b的值为：" + str(b/Z))
        print("c的值为：" + str(c/Z))
        print("d的值为：" + str(d/Z))
        print("e的值为：" + str(e/Z))
        print("w的值为：" + str(w/Z))
        print("稀有的数量为：" + str(e))
        print("万能的数量：" + str(w))

if __name__ == '__main__':
    openMoney = OpenMoney()
    #openMoney.userOpenSakuraReward('qa1')
    #openMoney.hecheng('qa1')
    openMoney.userOpenSakuraReward('qa1')
