from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from log.logg.Logg import Log


class TikApp:
    def __init__(self):
        self.LOG = Log(log="TestTikTok").getlog()

    def getdriver(self):
        self.LOG.info("这是app启动参数")
        desired_caps = {}
        desired_caps['deviceName'] = "emulator-5554"  # 设备名
        desired_caps['platformName'] = "Android"  # 设备平台
        desired_caps['appPackage'] = "com.ss.android.ugc.aweme"  # 包名
        desired_caps['platforVersion'] = "6.0.1"  # 系统版本
        desired_caps['appActivity'] = ".main.MainActivity"  # 启动的activity
        desired_caps['noReset'] = "false"
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver

    def always_allow(self,elem=None):
        dirver = self.getdriver()
        self.LOG.error("定位app启动首页的弹窗")
        if elem in dirver.page_source():
            self.getdriver().find_element_by_id("")
        else:
            dirver.find_element_by_id()

    def homepage(self):
        self.LOG.info("手机权限的容许")
        start = self.getdriver()
        sleep(6)
        slways = self.always_allow()
        if slways == True:
            pass
        else:
            start.find_element_by_id("com.ss.android.ugc.aweme:id/m7").click()
            start.switch_to.alert.accept()
            sleep(2)
            start.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(1)
            start.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(1)
            start.find_element_by_id("com.ss.android.ugc.aweme:id/uc").click()
            return start

    # 获取屏幕的宽高
    def get_size(self):
        driver = self.homepage()
        size = driver.get_window_size()  # 获取屏幕的宽高
        print(size)
        width = size['width']  # 获取高
        height = size['height']  # 宽
        return width, height

    # 向上滑动
    def swipe_up(self):
        swipe_up = self.get_size()
        sleep(2)
        x1 = swipe_up[0] / 2
        y1 = swipe_up[1] / 10 * 9
        x = swipe_up[1] / 10
        swipe_up.swipe(x1, y1, x1, x)


if __name__ == '__main__':
    T = TikApp()
    for i in range(10):
        T.swipe_up()
        if i == 10:
            break
        print("程序执行完毕")


