#参数化
import pytest
def add_function(a,b):
    return a+b

# @pytest.mark.parametrize("a,b,expected",[
#     (3,5,8),(-1,-2,-3),(1000,2000,2000)
# ],ids=["int","minus","bigint"])
# def test_add(a,b,expected):
#     assert add_function(a,b) == expected
#     print("这是我的第一个测试用例")


# @pytest.mark.parametrize("a",[0,1])
# @pytest.mark.parametrize("b",[2,4])
# def test_add(a,b):
#     print("ceshi: a->%s,b->%s"%(a,b))

