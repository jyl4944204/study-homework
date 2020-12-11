import pytest
import allure
import requests


# 1 运行执行的feature并将结果保存到本地的目录中：pytest test_link.py -vs --allure-features=""登录成功" --alluredir=./result2
# 2、生成allure测试报告并保存到本地：allure generate ./result2
# 3、生成报告到执行文件夹：allure generate ./result2 -o report

@allure.feature("搜索模块")
class TestSearch:

    @allure.story("搜索1")
    @allure.title("搜索1")
    def test_case1(self):
        print("case1")

    @allure.story("搜索2")
    @allure.title("搜索2")
    def test_case2(self):
        print("case2")


@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    @allure.title("测试成功")
    def test_login_success(self):
        with allure.step("步骤一：打开应用"):
            print("打开应用")
        with allure.step("步骤二：进入登录页面"):
            print("进入登录页面")
        with allure.step("步骤三：输入用户名和密码"):
            print("输入用户名和密码")

        print("这是第一个测试用例：登陆成功")

    @allure.story("登录失败")
    @allure.title("登录失败")
    def test_login_fail(self):
        assert 1 == 2

    @allure.story("用户名缺失")
    @allure.title("用户名缺失")
    def test_login_namelost(self):
        print("这是第三个测试用例：用户名缺失")
