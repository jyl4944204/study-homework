import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            # with open("../testcase/cookie.yaml","w",encodeing="UTF-8") as f:
            #     yaml.dump(self.driver.get_cookies(),f)
            self.cookie_login()

        else:
            self.driver = base_driver

    def cookie_login(self):
        """
        用cookie登录
        :return:
        """
        with open("../testcase/cookie.yaml") as f:
            cookies = yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")  # 跳转至主页
