from time import sleep

from selenium.webdriver.common.by import By

from poHomework.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        """
        保存成员信息
        :return:
        """
        from poHomework.page.contact_page import Contact

        self.driver.find_element_by_id("username").send_keys("jiang2")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("jiang2")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("15010236359")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2)
        self.driver.find_elements_by_css_selector("a.qui_btn.ww_btn.js_btn_save")[1].click()
        return Contact(self.driver).get_member()

    def add_member_fail(self, acctid, phone):
        """
        添加成员报错
        :return:
        """
        self.find(By.ID, "username").send_keys("jiang2")
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [i.text for i in res]
        return error_list
