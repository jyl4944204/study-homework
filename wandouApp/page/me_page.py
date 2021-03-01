from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from wandouApp.page.base_page import BasePage
from wandouApp.page.login_page import LoginPage


class MePage(BasePage):
    def goto_login_page(self):
        from wandouApp.page.main_page import MainPage
        sleep(5)
        eles = self.is_element_exist("点击登录")
        if eles == True:
            self.find_and_click(MobileBy.ID, "com.wonderfull.mobileshop:id/profile_user_photo")
            return LoginPage(self.driver)

        else:
            self.back_main_page()
            return MainPage(self.driver)

    def back_main_page(self):
        self.find_and_click(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView")

    def get_loginName(self):
        result = self.find(MobileBy.XPATH,"//*[@resource-id='com.wonderfull.mobileshop:id/profile_user_name']").text
        return result