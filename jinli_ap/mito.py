from time import sleep

from twisted.names import tap

from jinli_ap.start_app import Boot_file_Configuration


class Mitao_App(Boot_file_Configuration):

    def mitao_app(self):
        obj = self.get_driver(deviceName='ad93cc91',platformName='Android',appPackage='com.jinli.chatroom',
                        platforVersion=9,
                        appActivity='.activity.StartActivity',
                        noReset=False
                        )    # noReset=True
        sleep(3)
        return obj


    # 密码登录
    def login_user_password(self):
        login_obj = self.mitao_app()
        # 密码登录
        login_obj.find_element_by_id("com.jinli.chatroom:id/passwrod_login_tv").click()
        # 用户名
        login_obj.find_element_by_id("com.jinli.chatroom:id/et_phone").send_keys("15147938274")
        # 密码
        login_obj.find_element_by_id("com.jinli.chatroom:id/et_password").send_keys("000000l")
        # 同意用户协议
        login_obj.find_element_by_id("com.jinli.chatroom:id/checkbox_agreement").click()
        sleep(3)
        # 协议弹窗
        login_obj.find_element_by_id("com.jinli.chatroom:id/tv_confirm").click()
        # 登录
        login_obj.find_element_by_id("com.jinli.chatroom:id/tv_submit").click()
        sleep(4)
        # 照片设备
        login_obj.find_element_by_id("android:id/button1").click()
        # 录音
        login_obj.find_element_by_id("android:id/button1").click()
        # 青少年弹窗
        login_obj.find_element_by_class_name("android.widget.TextView").click()
        # 我的
        login_obj.find_element_by_id("com.jinli.chatroom:id/iv_icon").click()
        sleep(2)
        # 我的派对
        login_obj.find_element_by_id("com.jinli.chatroom:id/tv_my_party").click()
        # 我的房间
        login_obj.find_element_by_class_name("android.widget.FrameLayout").click()


if __name__ == '__main__':
    obj = Mitao_App()
    obj.login_user_password()
