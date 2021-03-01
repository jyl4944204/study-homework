import pytest
import yaml
from pythoncode.calculator import Calculator


# 加法测试
def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas, add_ids]


@pytest.mark.parametrize("a,b,expect", get_datas()[0])
def test_add( a, b, expect):
    assert expect == a + b

