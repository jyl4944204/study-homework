from time import sleep
import pytest
import yaml
import allure
from selenium import webdriver


class Test_weworkClass():

    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(10)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    #     # 获取cookie
    #     with open("cookie.yaml") as f:
    #         cookies = yaml.safe_load(f)
    #         for cookie in cookies:
    #             self.driver.add_cookie(cookie)
    #
    #     # 进入通讯录页面
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    #     sleep(5)
    #     # 点击添加成员按钮
    #     self.driver.find_elements_by_css_selector("a.qui_btn.ww_btn.js_add_member")[2].click()
    #
    # def teardown(self):
    #     self.driver.quit()

    # 获取cookie
    @allure.title("获取cookie并保存到yaml文件中")
    def test_get_cookies(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = driver.get_cookies()
        print(cookies)
        with open("cookie.yaml", "w", encoding="UTF-8", ) as f:
            yaml.dump(cookies, f)

    @allure.title("添加成员页面元素为空验证")
    def test_notnull(self):
        # 定位到姓名输入框
        user_name = self.driver.find_element_by_id("username")
        # 姓名输入框右键-失去焦点
        self.driver.execute_script("arguments[0].blur();", user_name)
        # 获取姓名为空后的提示内容
        username = self.driver.find_elements_by_css_selector("div.ww_inputWithTips_tips")[0].text
        # 断言提示内容是否为“请填写姓名”
        with allure.step("步骤一：断言当姓名为空时，提示内容为“请填写姓名"):
            assert username == u'请填写姓名'

        # 获取账号元素
        acct_id = self.driver.find_element_by_id("memberAdd_acctid")
        # 账号元素输入框右键-设置焦点
        self.driver.execute_script("arguments[0].focus();", acct_id)
        sleep(3)
        self.driver.execute_script("arguments[0].blur();", acct_id)
        sleep(3)
        # 获取账号为空后的提示内容
        acctid = self.driver.find_elements_by_css_selector("div.ww_inputWithTips_tips")[2].text
        # 断言提示内容是否为"请填写账号"
        with allure.step("步骤二：断言当账号为空时，提示内容为“请填写账号"):
            assert acctid == u'请填写帐号'

        # 获取手机元素memberAdd_phone
        phone = self.driver.find_element_by_id("memberAdd_phone")
        # 手机元素输入框-设置焦点
        self.driver.execute_script("arguments[0].focus();", phone)
        sleep(3)
        self.driver.execute_script("arguments[0].blur();", phone)
        sleep(3)
        # 获取手机为空后的提示内容
        member_phone = self.driver.find_elements_by_css_selector("div.ww_inputWithTips_tips")[3].text
        # 断言提示内容是否为"手机和邮箱不能同时为空"
        with allure.step("步骤三：断言当手机为空时，提示内容为手机和邮箱不能同时为空"):
            assert member_phone == u'手机和邮箱不能同时为空'

    @pytest.mark.parametrize("a", [("1501021635"), ("150102163590"), ("rtr24324")], ids=["10位验证", "12位验证", "非数字验证"])
    @allure.title("手机格式验证")
    def test_phone(self, a):
        sleep(3)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(a)
        phone = self.driver.find_element_by_id("memberAdd_phone")
        self.driver.execute_script("arguments[0].blur()", phone)
        sleep(3)
        member_phone = self.driver.find_elements_by_css_selector("div.ww_inputWithTips_tips")[3].text
        sleep(3)
        assert member_phone == u'请填写正确的手机号码'

    @allure.title("添加成员测试")
    def test_add_member(self):
        with open("add_number.yaml") as f:
            add_number_datas = yaml.safe_load(f)
            for add_number_data in add_number_datas:
                user_name = add_number_data["username"]
                acct_id = add_number_data["acct_id"]
                phone = add_number_data["phone"]
                with allure.step("步骤一：输入用户名"):
                    self.driver.find_element_by_id("username").send_keys(user_name)
                    sleep(2)
                with allure.step("步骤二：输入账号"):
                    self.driver.find_element_by_id("memberAdd_acctid").send_keys(acct_id)
                    sleep(2)
                with allure.step("步骤三：输入手机"):
                    self.driver.find_element_by_id("memberAdd_phone").send_keys(phone)
                    sleep(2)
                with allure.step("步骤四：把页面拖拖到底部"):
                    # 把页面拖到底部
                    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    sleep(2)
                with allure.step("步骤五：点击保存按钮"):
                    self.driver.find_elements_by_css_selector("a.qui_btn.ww_btn.js_btn_save")[1].click()
                    sleep(2)
                with allure.step("步骤六：断言是否保存成功"):
                    # 断言是否存在“保存成功”
                    assert u"保存成功" == self.driver.find_element_by_id("js_tips").text
                # 进入通讯录页面
                self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
                sleep(5)
                # 点击添加成员按钮
                self.driver.find_elements_by_css_selector("a.qui_btn.ww_btn.js_add_member")[2].click()
