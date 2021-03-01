from appium import webdriver

from wandouApp.page.base_page import BasePage
from wandouApp.page.main_page import MainPage

class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.wonderfull.mobileshop"
            caps["appActivity"] = ".biz.homepage.MainActivity"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            caps["settings[waitForIdleTimeout]"] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)