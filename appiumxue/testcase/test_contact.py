from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间
        caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 操作在10内循环查找元素 默认每个0.5秒找一次
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_contact(self):
        sleep(4)
        contact_ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']")
        contact_ele.click()
        # 滑动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).' +
                                 'scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
        add_new_ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']")
        add_new_ele.click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys("chengrui2")
        # self.driver.find_element(MobileBy.XPATH,"//")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()

        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(MobileBy.XPATH, "//*[@text='女']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(
            "15012017890")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
