from selenium import webdriver
from Public_method.Assertion_test import ConfigParser_ini_obj
from Public_method.Location_element import To_elemenT_Location


class real_name_audit():
    def __init__(self):
        self.driver = webdriver
        self.url = 'http://47.103.100.111:8110/'
        self.ini_obj = ConfigParser_ini_obj()
        self.To_element = To_elemenT_Location

    def get_ini(self):
        ini_username = self.ini_obj.config_ini('backstage','username')
        ini_password = self.ini_obj.config_ini('backstage','password')
        ini_list = []
        ini_list.append(ini_username)
        ini_list.append(ini_password)
        print(ini_list)

        return ini_list

    def sign_in(self):
        driver = self.driver.Chrome()
        driver.get(self.url)
        return driver

    def login(self):
        ini_user = self.get_ini()
        login = self.sign_in()
        username = ini_user[0]
        password= ini_user[1]
        login.find_element_by_class_name("el-input__inner").send_keys(username)
        login.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/div/div/input').send_keys(password)
        login.find_element_by_class_name("el-form-item__content").click()
        return login

    # -------------------------
    def home_page(self):
        self.login()



if __name__ == '__main__':
    ret = real_name_audit()
    ret.home_page()


