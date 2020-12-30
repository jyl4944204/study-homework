from appium.webdriver.common.mobileby import MobileBy

from appiumxue.page.base_page import BasePage
from appiumxue.page.contact_add_page import ContactAddPage


class MemmberInviteMenuPage(BasePage):
    def add_member_menul(self):
        """
        手动添加成员信息
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAddPage(self.driver)
