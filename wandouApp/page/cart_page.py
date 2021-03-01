from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from wandouApp.page.base_page import BasePage
from wandouApp.page.pay_done_page import PayDonePage


class CartPage(BasePage):

    def addOne(self):
        print("加购一个商品")
        data = []
        orginal = self.getSum()
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/shopcart_item_edit_sum")
        sleep(3)
        current = self.getSum()
        sleep(3)
        data.append(orginal)
        data.append(current)
        return data


    def subOne(self):
        print("减一个商品")
        data=[]
        orginal = self.getSum()
        self.find_and_click(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]/android.widget.ImageView[1]")
        sleep(3)
        current = self.getSum()
        data.append(orginal)
        data.append(current)
        return data

    def getSum(self):
        print("获取数量")
        num = self.find(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView").text
        return num

    #进入到结算页
    def goto_pay_done(self):
        self.find_and_click(MobileBy.XPATH,"//*[contains(@text,'结算郑州保税仓')]")
        return PayDonePage(self.driver)
