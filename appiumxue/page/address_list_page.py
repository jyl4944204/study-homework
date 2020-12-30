from appium.webdriver.common.mobileby import MobileBy

from appiumxue.page.base_page import BasePage
from appiumxue.page.member_invite_menu_page import MemmberInviteMenuPage


class AddressListPage(BasePage):
    def click_addmember(self):
        """
        点击添加成员
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return MemmberInviteMenuPage(self.driver)
