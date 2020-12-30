from appium.webdriver.common.mobileby import MobileBy
from appiumxue.page.address_list_page import AddressListPage
from appiumxue.page.base_page import BasePage


class MainPage(BasePage):

    def goto_address(self):
        """
        进入通讯录页面
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return AddressListPage(self.driver)
