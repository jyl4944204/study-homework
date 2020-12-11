import pytest
import allure

# 测试报告中添加链接
TEST_CASE_LINK = 'http://m.qa4.inagora.org/'


@allure.testcase(TEST_CASE_LINK, ' 测试链接')
def test_with_testcase_link():
    pass
