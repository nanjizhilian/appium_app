import json
import random
import threading
import requests
from time import sleep
url = 'http://47.103.100.111:8090/v1/bonuspoolchatroom/getbonus'


def get_bonus(Numer):
    data = {
        'bizId':'432635304025919488',
        'number':str(Numer),
        'poolId':'432935148393205760',
        'roomId':'430418677263896576',
        'userId':'432635304025919488',
    }
    headers = {
        'Accept-Language':'zh-Hans-CN;q=1',
        'channel':'qq',
        'appVersionCode':'1',
        'appVersion':'2',
        'userId':'407527631920173056',
        'Accept':'*/*',
        'token':'c0beb048d55486c103245ad74daa865e',
        'imei':'45FECF8D585D03EF9792CC6526F32854',
        'Content-Type':'application/x-www-form-urlencoded',
        'osVersion':'9',
        'device':'2',
        'Accept-Encoding':'gzip',
        'User-Agent':'okhttp/3.11.0'
    }
    se = requests.post(url=url,data=data,headers=headers)
    print(se)
    return se


def ur():
    for frequency in range(1, 1000000):
        print('这是第', frequency, '次砸蛋')
        nums = random.choice([1, 10, 100])
        print('砸蛋：', nums)
        obj = get_bonus(nums)
        print(obj.json())
        obj = obj.json()
        for i in obj['data']['list']:
            data_list = []
            dname = i['name']
            bonusNumber = i['bonusNumber']
            list_ap = {'name': dname, 'bonusNumber': bonusNumber}
            data_list.append(list_ap)
            print("砸蛋礼物为:", dname, "砸蛋个数为:", bonusNumber, "个")
            with open('/Users/lw/django_1.11_lx/appium_app/smasheggs/zadan.csv', 'a', encoding='utf-8') as fp:
                for d in data_list:
                    fp.write('\n')
                    fp.write("砸蛋次数：" + str(nums))
                    fp.write("礼物名称：" + d['name'])
                    fp.write('礼物数量：' + str(d['bonusNumber']))
                fp.write('\n')
            if frequency > 1000000:
                break

# gmoney = 1000
# lock = threading.Lock()    # 创建一个锁
# def reaponse_json():
#     global gmoney
#     nums = random.choice([1,10,100])
#     nums_obj = get_bonus(nums)
#     nums_obj = nums_obj.json()  # 将返回来的数据转化成json
#     for json_get in nums_obj['data']['list']:
#         data_list = []
#         dname = json_get['name']
#         bonusNumber = json_get['bonusNumber']
#         list_ap = {'name': dname, 'bonusNumber': bonusNumber}
#         print(list_ap)
#         data_list.append(list_ap)
#         print(data_list)
#
#     # return nums_obj
#
#
# # def get_json():
#
#
# def main():
#
#     t1 = threading.Thread(target=reaponse_json())
#     t2 = threading.Thread(target=reaponse_json())
#     t1.start()
#     t2.start()
#
#
# if __name__ == '__main__':
#     for i in range(10000):
#         main()

