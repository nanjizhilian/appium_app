import csv
import json
import random
import requests
import lxml
from bs4 import BeautifulSoup
from time import sleep

# 砸蛋

# url = 'http://47.103.100.111:8090/v1/bonuspoolchatroom/getbonus'
url = 'http://47.103.100.111:8095/v1/bonuspoolchatroom/getbonus'

def get_bonus(Numer):
    data = {
        'bizId': '432635304025919488',
        'number': str(Numer),
        'poolId': '432935148393205760',
        'roomId': '430418677263896576',
        'userId': '432929824038850560',
    }
    headers = {
        'Accept-Language':'zh-Hans-CN;q=1',
        'channel':'qq',
        'appVersionCode':'1',
        'appVersion':'2',
        'userId':'432929824038850560',
        'Accept':'*/*',
        'token':'52dee55ab02c75c41bda425ef07c6370',
        'imei':'45FECF8D585D03EF9792CC6526F32854',
        'Content-Type':'application/x-www-form-urlencoded',
        'osVersion':'9',
        'device':'2',
        'Accept-Encoding':'gzip',
        'User-Agent':'okhttp/3.11.0'
    }
    se = requests.post(url=url,data=data,headers=headers)
    # print(se)
    return se


for frequency in range(1,1000000):
    print('这是第',frequency,'次砸蛋')
    num = random.choice([1,10,100])
    print('砸蛋：',num)
    # obj = get_bonus(num)
    # print(obj.json())
    # obj = obj.json()

    if frequency > 1000000:
        break

#
# def asd(csv_roomid,csv_userid,csv_pagenum,csv_pagesize):
#     headers = ['roomid', 'userid', 'pagenum', 'pagesize']
#
#     rows = [
#         {'roomid': csv_roomid,
#          'userid': csv_userid,
#          'pagenum': csv_pagenum,
#          'pagesize': csv_pagesize,
#          }
#     ]
#     with open("test.csv", "a+", newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         # 以读的方式打开csv 用csv.reader方式判断是否存在标题。
#         with open("test.csv", "r", newline="") as f:
#             reader = csv.reader(f)
#             if not [row for row in reader]:
#                 writer.writerow(headers)
#                 writer.writerow(rows)
#             else:
#                 writer.writerows(rows)
#
#
# if __name__ == '__main__':
#     asd('1','2','3','4')
#
#


