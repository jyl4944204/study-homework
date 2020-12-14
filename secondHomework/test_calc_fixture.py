import pytest
import yaml
import allure


def get_data(keys):
    with open("./calc.yml") as f:
        datas = yaml.safe_load(f)
        adddatas = datas[f"{keys}"]
        return adddatas


@pytest.mark.run(order=1)
@pytest.mark.parametrize("a,b,expect", get_data("adddatas"))
@allure.title("加法")
def test_addd(a, b, expect, myfixture):
    calc = myfixture
    assert expect == calc.add(a, b)


@pytest.mark.run(order=4)
@pytest.mark.parametrize("a,b,expect", get_data("subdatas"))
@allure.title("减法")
def test_sub(a, b, expect, myfixture):
    calc = myfixture
    assert expect == calc.sub(a, b)


@pytest.mark.run(order=2)
@pytest.mark.parametrize("a,b,expect", get_data("muldatas"))
@allure.title("乘法")
def test_mul(a, b, expect, myfixture):
    calc = myfixture
    assert expect == calc.mul(a, b)


@pytest.mark.run(order=3)
@pytest.mark.parametrize("a,b,expect", get_data("divdatas"))
@allure.title("除法")
def test_div(a, b, expect, myfixture):
    calc = myfixture
    assert expect == calc.div(a, b)
