from selenium.webdriver.common.by import By

from poHomework.page.base_page import BasePage


class AddDepartment(BasePage):
    # 获取部门列表信息
    def select_department(self, name):
        self.driver.find_elements_by_xpath('//form//a[@class="jstree-anchor"]')

    def add_department(self, name):
        """
        保存部门信息
        :return:
        """
        from poHomework.page.contact_page import Contact

        self.driver.find_element(By.NAME, "name").send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list span.ww_btn_Dropdown_arrow").click()
        self.driver.find_elements_by_xpath('//form//a[@class="jstree-anchor"]')[1].click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_btn_Blue[d_ck="submit"]').click()
        return Contact(self.driver).get_department()

    def add_department_fail(self, name):
        """
        添加部门报错信息
        :return:
        """
        self.driver.execute_script("var q=document.documentElement.scrollTop=1000;")
        from poHomework.page.contact_page import Contact
        self.driver.find_element_by_name("name").send_keys(name)
        name1 = self.driver.find_element_by_name("name")
        self.driver.execute_script("arguments[0].blur();", name1)
        self.driver.find_element(By.CSS_SELECTOR, '.ww_btn_Blue[d_ck="submit"]').click()
        res = self.driver.find_element_by_id("js_tips").text
        return res
