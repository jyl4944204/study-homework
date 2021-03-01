class GenerateOrder:

    def login(self):
        print("登录")

    def add_cart(self,goods_id):
        print("加入到购物车")

    def generateOrder(self,goods_id,house_id):
        self.login()
        self.add_cart(goods_id)
        self.generateOrder(goods_id,house_id)
        print("生成订单")
