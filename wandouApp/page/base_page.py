from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

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

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result
