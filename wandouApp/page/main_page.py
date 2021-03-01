from appium.webdriver.common.mobileby import MobileBy

from wandouApp.page.base_page import BasePage
from wandouApp.page.me_page import MePage
from wandouApp.page.search_page import SearchPage


class MainPage(BasePage):
    """
    进入我的页面
    """
    def goto_mePage(self):
        self.find_and_click(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.LinearLayout/android.widget.ImageView")
        return MePage(self.driver)

    def goto_searchPage(self):
        self.find_and_click(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        return SearchPage(self.driver)