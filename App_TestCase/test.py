import time
import requests
from Public_method.sign_test import sign


def test():
    itme = time.time()
    timestamp = int(itme)
    hander = {
         "appVersion": "2.0.5",
         "channel": "official",
         "device": 2,
         "imei": "45FECF8D585D03EF9792CC6526F32854",
         "osVersion": 9,
         "timestamp": timestamp,
         "appVersionCode": 26,
         "token": "39fbf596078a3953aa8d9ac2276d679b",
         "userId": "451023793608069120",
         "Host": "47.103.100.111:8095",
         "Accept-Encoding": "gzip",
         "User-Agent": "okhttp/3.11.0",
         "Connection": "keep-alive"
    }
    signstr=sign("appVersion2.0.5appVersionCode26Accept-Encodinggzipchannelofficialdevice2Connectionkeep-aliveimei45FECF8D585D03EF9792CC6526F32854osVersion9password123OK123secondPwd123OK123timestamp"+str(timestamp)+"token39fbf596078a3953aa8d9ac2276d679bUser-Agentokhttp/3.11.0userId451023793608069120Host47.103.100.111:8095")
    data = {
        "password":"123OK123",
        "secondPwd":"123OK123",
        "signstr":signstr,
        "timestamp": timestamp,
    }
    response = requests.post('http://47.103.100.111:8095/v1/user/secondaryPwd/setPassword',data,hander)
    print(response.text)
    print(response.url)


if __name__ == '__main__':
    pass

