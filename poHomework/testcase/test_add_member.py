import pytest

from poHomework.page.main_page import Main


class TestAddMember:

    def setup_class(self):
        self.main = Main()

    def test_add_member(self):
        res = self.main.goto_contact().goto_addMember().add_member()
        assert "jiang2" in res

    @pytest.mark.parametrize("acctid,phone,expect", [('jiang2', '15010216543', '该帐号已被“jiang2”占有'),
                                                     ('', '15010216543', '请填写帐号'),
                                                     ('jiang3', '', '手机和邮箱不能同时为空')
                                                     ])
    def test_add_member_fail(self, acctid, phone, expect):
        res = self.main.goto_contact().goto_addMember().add_member_fail(acctid, phone)
        assert expect in res
