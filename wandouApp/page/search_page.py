from appium.webdriver.common.mobileby import MobileBy

from wandouApp.page.base_page import BasePage
from wandouApp.page.goods_detail_page import GoodsDetailPage


class SearchPage(BasePage):

    def search_goods(self,searchkey):
        #输入面膜进行搜索
        self.find_and_send_keys(MobileBy.ID,"com.wonderfull.mobileshop:id/search_input",searchkey)
        #点击列表中的面膜
        self.find_and_click(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]")
        #进入到商品详情页
        self.find_and_click(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")
        return GoodsDetailPage(self.driver)
