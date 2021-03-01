from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy

from wandouApp.page.base_page import BasePage


class LoginPage(BasePage):
    """
    手机号密码登录成功
    """

    def login_by_password_success(self,user_name,password):

        from wandouApp.page.me_page import MePage

        self.mePage = MePage()

        self.find_and_click(MobileBy.XPATH,"//*[@text='密码登录']")
        sleep(5)
        #输入手机号
        self.find_and_send_keys(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText[1]",user_name)
        #输入密码
        self.find_and_send_keys(MobileBy.XPATH,"//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText[2]",password)
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/root_view")
        #返回到首页
        #self.mePage.back_main_page()

        return MePage(self.driver).get_loginName()

    """
    手机号密码登录失败
    """
    def login_by_password_fail(self,user_name,password):

        from wandouApp.page.me_page import MePage

        self.mePage = MePage()

        self.find_and_click(MobileBy.XPATH,"//*[@text='密码登录']")
        sleep(5)
        allure.step("输入手机号")
        #输入手机号
        self.find_and_send_keys(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText[1]",user_name)
        allure.step("输入密码")
        #输入密码
        self.find_and_send_keys(MobileBy.XPATH,"//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText[2]",password)
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/root_view")
        toast  =  self.get_toast_text()
        sleep(3)
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/top_back")
        sleep(3)
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/top_back")
        print(toast)
        #返回到首页
        #self.mePage.back_main_page()
        return toast

    """
    手机验证码登录成功
    """
    def login_by_verify_success(self):
        self.find_and_send_keys(MobileBy.ID,"com.wonderfull.mobileshop:id/phone_number_view","14477777701")
        self.find_and_click(MobileBy.ID,"com.wonderfull.mobileshop:id/root_view")
        #self.driver.find_elements_by_class_name("android.widget.TextView")[1].click()
        self.driver.find_elements_by_class_name("android.view.View")[1].send_keys("7")
        self.driver.find_elements_by_class_name("android.view.View")[2].send_keys("4")
        self.driver.find_elements_by_class_name("android.view.View")[3].send_keys("3")
        self.driver.find_elements_by_class_name("android.view.View")[4].send_keys("1")



        pass



