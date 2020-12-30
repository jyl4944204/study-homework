import time
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).' +
                                 'scrollIntoView(new UiSelector().text("打卡").instance(0))').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        WebDriverWait(self.driver, 10).until(lambda x: "123" in x.page_source)
        # print(self.driver.page_source)

        assert "外出打卡成功" in self.driver.page_source()
