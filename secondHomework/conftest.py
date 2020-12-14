import pytest
import yaml
from secondHomework.calcu import Caluctor


@pytest.fixture()
def myfixture():
    calc = Caluctor()
    yield calc
    # print("\n执行myfixture,里面的参数是:%s\n "% request.param)
    # yield request.param  #类似return操作
    # print("激活fixture里的teardown")
