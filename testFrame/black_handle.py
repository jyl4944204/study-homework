import logging

import allure
logging.basicConfig(level=logging.info())
#info > debug >error

def black_wrapper(fun):
    def run(*args,**kwargs):
        basepage = args[0]
        try:
            logging.info("start find: \nargs:" + str(args))
            return fun(*args,**kwargs)
        except Exception as e:
            basepage.screentshot("tmp.png")
            with open("./tmp.png",'rb') as f:
                pricture_data = f.read()
            allure.attach(pricture_data,attachment_type=allure.attachment_type.PNG)
            #遍历黑名单的元素进行处理
            for black in basepage.black_list:
                eles = basepage.finds(*black)
                if len(eles) > 0:
                    #对黑名单元素进行点击，可以自由扩展
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run
