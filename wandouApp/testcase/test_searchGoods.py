from wandouApp.page.app import App

class TestSearchGoods:
    def setup_class(self):
        self.app = App()
        self.app.start()

    def test_search_goods(self):
        self.app.goto_main().goto_searchPage().search_goods("洗面奶")
