import pytest
from pythoncode.calculator import Calculator


# 参数化练习
class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")
    def teardown_class(self):

        print("结束")
    #加法测试
    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(100,300,400)],ids=["int_add","minu_add",'bigint_add'])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)
    #减法测试
    @pytest.mark.parametrize("a,b,expect", [(3, 5, -2), (-1, -2, 1), (100, 300, -100)],
                             ids=["int_sub", "minu_sub", 'bigint_sub'])
    def test_sub(self,a,b,expect):
        assert expect == self.calc.sub(a,b)
    #乘法测试
    @pytest.mark.parametrize("a,b,expect",[(1,1,1),(-1,-2,2),(1,0,0)],ids=["int_mul","minu_mul",'0_mul'])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)
    # 除法测试
    @pytest.mark.parametrize("a,b,expect", [(1, 1, 1), (-2, -1, 2), (0, 1, 0)], ids=["int_div", "minu_div", '0_mul'])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)
