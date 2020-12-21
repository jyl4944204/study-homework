from time import sleep

from selenium.webdriver.common.by import By

from poHomework.page.add_department_page import AddDepartment
from poHomework.page.base_page import BasePage


class Contact(BasePage):
    def goto_addMember(self):
        """
        跳转到添加成员页面
        :return:
        """
        pass

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
