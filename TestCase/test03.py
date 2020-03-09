import requests
import random


def reword(userid,kwargs):
    url = "http://47.103.100.111:8094/v1/chatroom/reward/reward"
    data = {
        "roomId": 430408485969203200,
        "giftId": 396660648995590186,
        "number": 1,
        "toUids": kwargs,
        "bizId":"",
        "userId": userid,
        "type": 1,
        "signstr": "59504ab01496b13c2c8d9a75a09717d1",
        "token": "9a8ce9db524533978a0b26e309028d7d",
    }
    response = requests.post(url=url,data=data)
    print(response)
    response.json()


if __name__ == '__main__':
    for i in range(1,20):
        toUids = "430404543524769792", "431857742953713664", "431857495963734016", "431851753017839616","431873844194709504", "430093063176720384", "431123273061896192",
        touids = ("430084416136679424","430093063176720384","430093417427636224","430105073188737024","430359700362629120",
                  "430388911878049792","431171314020126720","431174923772366848","431176459839737856","431177892983083008")
        to = random.choice(touids)
        print("to=",to)
        reword(to,toUids)
        print(toUids)


