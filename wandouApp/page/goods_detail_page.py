from time import sleep

import allure
import pytest
from appium.webdriver.common.mobileby import MobileBy

from wandouApp.page.base_page import BasePage
from wandouApp.page.cart_page import CartPage

class GoodsDetailPage(BasePage):
    """
    添加到购物车
    """
    def add_cart(self):
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/goods_detail_addToCart")
        sleep(3)
        if "com.wonderfull.mobileshop:id/pop_sku_ok" in self.driver.page_source:
            self.find_and_click(MobileBy.ID, "com.wonderfull.mobileshop:id/pop_sku_ok")
            self.find_and_click(MobileBy.ID, "com.wonderfull.mobileshop:id/goods_detail_cart")
        else:
            # 进入到购物车页面
            self.find_and_click(MobileBy.ID, "com.wonderfull.mobileshop:id/goods_detail_cart")
        self.back_main()
        return CartPage(self.driver).get_toast_text()
    """
    加入购物车后，返回首页
    """
    def back_main(self):
        sleep(3)
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/top_view_back")
        # 返回到首页
        self.find_and_click(MobileBy.ID, "com.wonderfull.mobileshop:id/goods_detail_header_back_bg")
        sleep(3)
        self.find_and_click(MobileBy.ID, "com.wonderfull.mobileshop:id/top_view_back")
    """
    立即购买
    """
    def buy_now(self):
        #如果存在立即购买按钮，则点击立即购买按钮
        sleep(3)
        if "立即购买" in self.driver.page_source:
            self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/goods_detail_buy_now")
            self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/pop_sku_ok")
            sleep(3)
            page_source = self.driver.page_source
            return page_source
        else:
            return "无立即购买按钮"

    """
    点击立即购买之后返回首页
    """
    def buy_now_back_main(self):
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/top_view_back")
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/dialog_ok")
        sleep(3)
        # 返回到首页
        self.find_and_click(MobileBy.ID, "com.wonderfull.mobileshop:id/goods_detail_header_back_bg")
        sleep(3)
        self.find_and_click(MobileBy.ID, "com.wonderfull.mobileshop:id/top_view_back")

