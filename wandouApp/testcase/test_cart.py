from wandouApp.page.app import App
from wandouApp.page.cart_page import CartPage


class TestCart:
    def setup_class(self):
        self.app = App()
        self.app.start()
        self.cart = CartPage()

    #增加一个商品，并断言加购后的数量是否正确
    def test_addOne(self):
        data = self.app.goto_main().goto_mePage().goto_login_page().goto_searchPage().search_goods().add_cart().addOne()
        onginal = int(data[0])
        num = int(data[1])
        assert num == onginal + 1

    #减一个商品,并断言减后的数量是否正确
    def test_subOne(self):
        data = self.cart.subOne()
        onginal = int(data[0])
        num = int(data[1])
        assert num == onginal - 1

    def test_goto_pay_done(self):
        pass



