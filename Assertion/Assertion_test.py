from jinli_ap.start_app import Boot_file_Configuration
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待包
import configparser
"""
利用启动页面的来控制时间等待
"""


class AndroidDriverWait(Boot_file_Configuration):

    # 隐士等待
    def wait_driver(self,number):
        wait = AndroidDriverWait.get_driver()

        if number == None:

            wait.implicitly_wait(5)
            print("贾维斯：\t：先生，正在启动隐士等待")

        else:
            wait.implicitly_wait(number)

    # 显示等待
    def wait_dr(self,numbers):

        dr = AndroidDriverWait.get_driver()

        if numbers == None:

            WebDriverWait(dr,5,0.5) #  设置5秒等待时间，每0.1秒询问一次
            print("贾维斯：\t>>>先生，显示等待启动")

        else:
            WebDriverWait(dr,6,1)


# ini配置文件
class ConfigParser_ini_obj():

    def config_ini(self,title,key):
        open_ini ='/Users/lw/django_1.11_lx/appium_app/config/Loal_Eelement.ini'
        config = configparser.ConfigParser()
        open_obj = config.read(open_ini)
        config.read(open_obj)
        title = config[title][key]
        return title


if __name__ =='__main__':

    ob = ConfigParser_ini_obj()
    ret = ob.config_ini('jinli_signin_element','password_sigin')
    print(ret)


