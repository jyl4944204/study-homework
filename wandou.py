import requests
data = {
  "method" : "ErpApi.getPurchasePriceByJancode",
  "ch" : "default",
  "device_token" : "12680f1ee0ce51af3533e07738822fc7828d84468a09cb478ffd55b1ef73e34d",
  "devid" : "554a7d191620d80184d728e4fdcbcd2c",
  "devname" : "",
  "devtype" : "iphone",
  "dpi" : "1242x2208",
  "idfa" : "B652994D-0853-458E-ACDF-82ADC45FEB5E",
  "img_fmt" : "webp",
  "lang" : 'zh-Hans-CN',
  "model" : 'iPhone10',
  "network_type" : "wifi",
  "os_version" : '11.2.1',
  "rtick" : '1533095807.635513',
  "sign" : "11111",
  "sm_devid" : "20180320155029773fe3fd95f93832022fb0a52336e37001b2ec02f7020928",
  "tz" : '28800',
  "user_id" : '2187879',
  "v" : '5.2.2',
  "wake_type" : 'normal',
  "jancode" : '4901301254276',
}
for key in data.sort():
    print (key)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Connection' : 'keep-alive',
    'Cookie' :'user_key=30d5700524b9313badb7009e7c7fdade; UM_distinctid=164ea9bf5cb306-0b8fabae57c9898-e3c496c-4a640-164ea9bf5cc1b2; duty_free=0',
};
request = requests.get("https://mapi.wandougongzhu.cn",data,)