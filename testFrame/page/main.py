import yaml

from testFrame.base_page import BasePage


class Main(BasePage):

    def goto_market(self):
        self.load("../page/main.yaml")