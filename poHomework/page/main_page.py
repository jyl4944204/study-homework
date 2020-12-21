from selenium.webdriver.common.by import By

from poHomework.page.base_page import BasePage


class Main(BasePage):

    def goto_contact(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        """
        跳转到通讯录页面
        :return:
        """
        from poHomework.page.contact_page import Contact
        return Contact(self.driver)

    def goto_addMember(self):
        """
        跳转到添加成员页面
        :return:
        """
