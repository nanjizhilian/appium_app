import requests
from Public_method.sign_test import sign
from Public_method.start_app import Boot_file_Configuration


class login():
    def __init__(self):
        self.Boot = Boot_file_Configuration()

    def get_code(self):
        number = self.Boot.generate_number()
        sign_str = "mobile=" + number + '&' + '76576076c1f5f657b634e966c8836a06'
        sign_ret = sign(sign_str)
        url = 'http://v.qingchan.vip:8081/api/public/?'
        data = {
            'service': "Login.GetCaptchaLoginCode",
            'mobile': number,
            'sign': sign_ret,

        }
        print(number)
        response = requests.get(url,params=data)
        print(response.text)


if __name__ == '__main__':
    obj = login()
    obj.get_code()



