import yaml


# def b(fun):
#     def run(*args,**kwargs):
#         print("a1")
#         fun(*args,**kwargs)
#         print("a2")
#     return run

def test_yaml():
    with open("./tmp.yaml",'r',encoding="utf-8") as f:
        data = yaml.load(f)
        #字典
        #print(data['a'])
        print(data[0])
