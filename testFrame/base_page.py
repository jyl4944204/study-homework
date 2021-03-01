import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from testFrame.black_handle import black_wrapper


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        #参考：黑名单类
        self.black_list = [(MobileBy.XPATH,"//*[@resource-id=''comiiee]")]


    def finds(self,by,locator):
        self.driver.find_elements(by,locator)

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)


    def find_and_click(self, by, locator):
        return self.driver.find_element(by, locator).click()

    def scroll_find(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).' +
                                 'scrollIntoView(new UiSelector().'f'text("{text}").instance(0))')

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def swip_find(self, by, loator):
        eles = self.driver.find_elements(by, loator)
        while len(eles) > 0:
            eles = self.driver.find_elements(by, loator)
        return eles[0]

    def find_and_send_keys(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def wait_for(self, by, locator):
        def wait_ele_for(by, locator):
            eles = self.driver.find_elements(by, locator)
            return len(eles) > 0

    def load(self,yaml_path):
        with open(yaml_path, encoding='utf-8') as f:

            data = yaml.load(f)
        # step: find ,action
        for step in data:
            xpath_expr = step.get("find")
            action = step.get("action")
            if action == "find_and_click":
                self.find_and_click(xpath_expr, action)
            elif action == "send":
                content = step.get('content')
                self.send(xpath_expr, action, content)

    def start
    def screentshot(self,picture_path):
        self.driver.save_screenshot(picture_path)
