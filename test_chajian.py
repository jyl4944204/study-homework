#mark标记
#pytest -sv -m "demo or smoke" test_mark.py  只要有任意一个标记就执行
#pytest -sv -m "demo and smoke" test_mark.py  一个函数两个标记都打上才执行
#pytest -sv -k "two" test_mark.py  匹配名字执行
#pytest --collect-only test_mark.py  收集参数不执行
#pytest.assume(1 == 1) 多重校验  依次执行 pytest-assume
#pytest -n 6 test_chajian 几个cpu并发执行
#@pytest.mark.run(order=2)  指定用例执行顺序   pytest-ording


import pytest
class Test_demo():
    @pytest.mark.run(order=2)
    def test_one(self):
        a = 5
        b = -1
        assert a != b
        assert 1 != 1
        assert 2 != 2
        print("我的第一个测试用例")

    @pytest.mark.run(order=1)
    def test_three(self):
        a = 5
        b = 2
        assert a != b
        print("我的第三个测试用例")
    @pytest.mark.demo
    def test_two(self):
        a = 5
        b = 2
        pytest.assume (1 == 1)
        pytest.assume (1 == 1)
        pytest.assume (1 == 1)

        print("我的第二个测试用例")
