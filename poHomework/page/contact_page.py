from time import sleep

from selenium.webdriver.common.by import By
from poHomework.page.add_department_page import AddDepartment
from poHomework.page.base_page import BasePage

class Contact(BasePage):
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_memberList = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    def goto_addMember(self):
        """
        跳转到添加成员页面
        :return:
        """
        from poHomework.page.add_memeber_page import AddMember
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def get_department(self):
        """
        跳转到添加部门页面
        :return:
        """
        sleep(5)
        elements = []
        for element in self.driver.find_elements_by_css_selector(".jstree-anchor"):
            elements.append(element.text)
        return elements

        # return [element.text for element in self.driver.find_element(By.CSS_SELECTOR,"jstree-anchor")]

    def goto_department(self):
        """
        跳转到添加部门页面
        :return:
        """
        # self.driver.find_element(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        sleep(5)
        self.driver.find_element_by_css_selector(".member_colLeft_top_addBtn").click()
        # self.driver.find_element(By.CSS_SELECTOR,".js_create_party").click()
        self.driver.find_element_by_css_selector(".js_create_party").click()
        return AddDepartment(self.driver)
        pass

    """
    获取列表信息
    """

    def get_member(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        member_list = self.finds(*self._location_memberList)
        member_list_res = []
        for i in member_list:
            print(i.text)
            member_list_res.append(i.text)
        print(member_list_res)
        return member_list_res
