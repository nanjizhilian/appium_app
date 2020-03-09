import random
from asyncio import sleep
from jinli_ap.start_app import Boot_file_Configuration
from Assertion.Assertion_test import ConfigParser_ini_obj

class jinli_app():
    def __init__(self):
        self.Bos = Boot_file_Configuration()
        self.Config=ConfigParser_ini_obj

    def get_jinli_login(self):
        init_jinli = Boot_file_Configuration()
        obj = init_jinli.get_driver(deviceName='ad93cc91',# '.activity.MainActivityV2',
                                           platformName='Android',
                                           appPackage='com.jinli.chatroom',
                                           platforVersion=9,
                                           appActivity='com.jinli.chatroom.activity.StartActivity'
                                           )    # noReset=True
        sleep(3)
        print(type(obj))
        return obj

    def login_password(self):
        """
        密码登录
        :return:
        """
        cofig_obj = self.Config()
        element_id = cofig_obj.config_ini('jinli_signin_element','segnin_PassWord')
        login_obj=self.get_jinli_login()
        # 密码登录按钮
        login_obj.find_element_by_id(element_id).click()
        # 手机号
        element_ids = cofig_obj.config_ini("jinli_signin_element",'VerificationCode')
        login_obj.find_element_by_id(element_ids).send_keys('username_password','username')
        # 手机键盘回收
        login_obj.keyevent(4)
        # 密码
        password = cofig_obj.config_ini("username_password",'password')
        login_obj.find_element_by_id(password).send_keys()
        # 协议同意
        agreement = cofig_obj.config_ini("jinli_signin_element",'agreement')
        login_obj.find_element_by_id(agreement).click()
        # 登录
        sogini = cofig_obj.config_ini("jinli_signin_element",'sigini')
        login_obj.find_element_by_id(sogini).click()

        return login_obj


    # 房间砸蛋
    def Smash_eggs(self):
        eggs=self.get_jinli_login()
        # 砸蛋
        eggs.find_element_by_id("com.jinli.chatroom:id/egg_action").click()
        # 砸金蛋
        eggs.find_element_by_id("com.jinli.chatroom:id/rl_gold").click()
        while True:
            for frequency in random.choice([1,10,100]):
                print("砸次次数为:",frequency)
                if frequency == 1:
                    # 一次
                    eggs.find_element_by_id("com.jinli.chatroom:id/iv_play_one").click()
                    print("砸蛋一次成功")
                    sleep(1)
                elif frequency == 10:
                    # 10次
                    eggs.find_element_by_id("com.jinli.chatroom:id/iv_play_ten").click()
                    # 收入背包
                    eggs.find_element_by_id("com.jinli.chatroom:id/tv_btn").click()
                    print("砸蛋10次成功")
                elif frequency == 100:
                    # 100次
                    eggs.find_element_by_id("com.jinli.chatroom:id/iv_play_hun").click()
                    # 收入背包
                    eggs.find_element_by_id("com.jinli.chatroom:id/tv_btn").click()
                    print("砸蛋100次成功")


if __name__ == '__main__':
    obj = jinli_app()
    obj.login_password()







