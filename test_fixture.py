import pytest
#可以跨文件使用   登录可以用


class Test_demo():
    def test_one(self,myfixture):
        print("执行test_one")
        myenv = myfixture
        print(myenv)
        #assert 1+1==2

    def test_two(self,myfixture):
        print("执行test_two")
        assert 1 + 1 == 2

    def test_three(self):
        print("执行test_three")
        assert 1 + 1 == 2

