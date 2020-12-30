from appiumxue.page.app import App


class TestAddMember:
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        pass

    def test_add_member(self):
        result = self.app.goto_main().goto_address().click_addmember().add_member_menul().add_member()
        assert result
