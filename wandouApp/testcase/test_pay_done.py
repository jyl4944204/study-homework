import allure

from wandouApp.page.app import App
class TestPayDone:
    def setup_class(self):
        self.app = App()
        self.app.start()

    allure.title("结算")
    def test_pay_done(self):
        data1 = self.app.goto_main().goto_mePage().goto_login_page().goto_searchPage().search_goods().add_cart().goto_pay_done().pay_done()
        #data = self.app.goto_main().goto_mePage().goto_login_page().login().goto_searchPage().goto_goodsDetail().add_cart().goto_pay_done()

