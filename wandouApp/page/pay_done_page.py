from appium.webdriver.common.mobileby import MobileBy

from wandouApp.page.base_page import BasePage


class PayDonePage(BasePage):
    #支付
    def pay_done(self):
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/check_order_submit")
        return True