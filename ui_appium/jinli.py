import time
from Public_method.start_app import Boot_file_Configuration
from config.app_parameter import password_Signin
from handle.user_data import user_data


class stop_app():
    def __init__(self):
        self.star_obj = Boot_file_Configuration()
        self.get_driver = self.star_obj.get_driver()

    def signin(self):
        sig = self.get_driver()
        time.sleep(3)
        sig.find_element_by_id(password_Signin.useriphone_id).send_keys(user_data.cell_phone_number)
        sig.find_element_by_id(password_Signin.useriphone_id).send_keys(user_data.password)
        sig.find_element_by_id(password_Signin.useragreement_id).click()
        sig.find_element_by_id(password_Signin.signin_id).click()
        # WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.tal.kaoyan:id/login_register_text'))
        # driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
        print("登录完毕！请指示")


if __name__ =="__main__":
    obj = stop_app()
    obj.get_driver("f8846199","Android","com.jinli.chatroom","9","com.jinli.chatroom.activity.StartActivity")


