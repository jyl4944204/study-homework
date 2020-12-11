import pytest
import allure


# 指定级别运行测试用例：>pytest test_sevennity.py --allure-severities="normal" -vs
# 本地开启服务指定端口号供其他人查看 allure open -h 10.0.0.104 -p 8883 ./allure-report
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("方法普通级别的测试")
def test_with_trivial_senvirty():
    pass


@allure.severity(allure.severity_level.NORMAL)
@allure.title("方法一般级别的测试")
def test_with_trivial_normal():
    print("method normal")
    pass


@allure.severity(allure.severity_level.NORMAL)
@allure.title("类级别的测试")
class TestClassWithNormalSeverity(object):
    @allure.title("方法无级别的测试")
    def test_inside_the_normal_senverity_test_class(self):
        print("class")
        pass

    @allure.title("类里边的普通级别的测试")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_inside_the_trivial_senverity_test_class(self):
        print("class trival")
        pass
