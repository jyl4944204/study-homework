#此文件名固定不可更改，一般登录链接DB可以放到此文件中
#如果放到文件夹中，文件夹应该有-init-文件
# fixture(autouse="true")  这个参数不传也会执行
# fixture(scope="class")  只在类里执行一次
# yield前相当于setup，后相当于teardown
#%s 是格式化
import requests
import pytest
@pytest.fixture(params=["参数1","参数2"])
def myfixture(request):
    print("\n执行myfixture,里面的参数是:%s\n "% request.param)
    yield request.param  #类似return操作
