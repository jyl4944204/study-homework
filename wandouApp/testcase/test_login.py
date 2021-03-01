import allure
import pytest

from wandouApp.page.app import App
from wandouApp.page.cart_page import CartPage


class TestLogin:
    def setup_class(self):
        self.app = App()
        self.app.start()
        self.cart = CartPage()

    allure.title("手机号密码登录成功")
    @pytest.mark.run(order=2)
    def test_login_by_password_success(self):
        result = self.app.goto_main().goto_mePage().goto_login_page().login_by_password_success("15010216358","jyl4944204")
        assert result == "倔倔1"

    allure.title("手机号密码登录失败")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("user_name,password,expect",[(15010216358,"jyl4944203","用户名或密码错误"),(15010216359,"jyl4944204","用户名或密码错误")],ids=["密码错误","用户名错误"])
    def test_login_by_password_fail(self,user_name,password,expect):
        print("手机密码登录失败case")
        result = self.app.goto_main().goto_mePage().goto_login_page().login_by_password_fail(user_name,password)
        assert expect == result


