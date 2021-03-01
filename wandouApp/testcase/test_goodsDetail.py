from time import sleep

import allure
import pytest
from appium.webdriver.common.mobileby import MobileBy

from wandouApp.page.app import App
from wandouApp.page.goods_detail_page import GoodsDetailPage


class TestGoodsDetail:

    def setup_class(self):
        self.app = App()
        self.app.start()
        self.goodsDetail = GoodsDetailPage()


    @pytest.fixture(scope="function",autouse=False)
    def teardown(self):
        yield
        self.goodsDetail.back_main()

    pytest.mark.run(order=1)
    allure.title("加入购物车")
    def test_add_cart(self):
        toast = self.app.goto_main().goto_searchPage().search_goods("面膜").add_cart()
        assert "已加入购物袋" in toast


    pytest.mark.run(order=2)
    allure.title("立即购买")
    def test_by_now(self):
        page_source = self.app.goto_main().goto_searchPage().search_goods("面膜").buy_now()
        assert "确认支付" in page_source
        self.goodsDetail.buy_now_back_main()