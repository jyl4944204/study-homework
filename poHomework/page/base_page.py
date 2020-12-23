import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

    def find(self, by, value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=value)

    def wait_click(self, locator):
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))
