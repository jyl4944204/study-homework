#mark标记
#pytest -sv -m "demo or smoke" test_mark.py  只要有任意一个标记就执行
#pytest -sv -m "demo and smoke" test_mark.py  一个函数两个标记都打上才执行
#pytest -sv -k "two" test_mark.py  匹配名字执行
#pytest --collect-only test_mark.py  收集参数不执行

import pytest
class Test_demo():
    @pytest.mark.demo
    @pytest.mark.smoke
    def test_one(self):
        a = 5
        b = -1
        assert a != b
        print("我的第一个测试用例")

    @pytest.mark.smoke
    def test_demo1(self):
        a = 5
        b = 2
        assert a != b
        print("我的第三个测试用例")
    @pytest.mark.demo
    def test_two(self):
        a = 5
        b = 2
        assert a != b
        print("我的第二个测试用例")
