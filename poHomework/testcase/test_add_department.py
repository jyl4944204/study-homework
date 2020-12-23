from time import sleep

from poHomework.page.main_page import Main
import pytest


class TestAddDepartment:

    def setup_class(self):
        self.main = Main()

    def test_add_Department(self):
        """
        测试添加部门
        :return:
        """
        name = "gg"
        res = self.main.goto_contact().goto_department().add_department(name)
        assert name in res

    @pytest.mark.parametrize("name,expect", [("jiang9", "请选择所属部门")])
    def test_add_department_fail(self, name, expect):
        """
        测试添加部门报错信息
        :return:
        """
        sleep(5)
        res = self.main.goto_contact().goto_department().add_department_fail(name)
        assert expect in res
