from time import sleep
from appium import webdriver
import random
import configparser  #配置文件
import csv
import hashlib

class Boot_file_Configuration():

    def get_driver(self,deviceName=None,
                   platformName=None,
                   appPackage=None,
                   platforVersion=None,
                   appActivity=None,
                   noReset=None):
        desired_caps = {}
        desired_caps['deviceName'] = deviceName # 设备名
        desired_caps['platformName'] = platformName # 设备平台
        desired_caps['appPackage'] = appPackage # 包名
        desired_caps['platforVersion'] = platforVersion # 系统版本
        desired_caps['appActivity'] = appActivity   # 启动的activity
        desired_caps['noReset'] = noReset
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        return driver

    # 获取屏幕的宽高
    def get_size(self):
        driver = self.get_driver()
        size = driver.get_window_size()  # 获取屏幕的宽高
        print(size)
        width = size['width']   # 获取高
        height = size['height'] # 宽
        return width,height

    # 向左滑动
    def swipe_life(self):
        swipe_li = self.get_size()
        sleep(2)
        x1 = swipe_li[0] / 10 * 9
        y1 = swipe_li[1] / 2
        x = swipe_li[2] / 10
        swipe_li.swipe(x1, y1, x, y1)

    # 像右滑动
    def swipe_right(self):
        swipe_right = self.get_size()
        sleep(2)
        x1 = swipe_right[0] / 10
        y1 = swipe_right[1] / 2
        x = swipe_right[2] / 10 * 9
        swipe_right.swipe(x1, y1, x, x1)

    # 向上滑动
    def swipe_up(self):
        swipe_up = self.get_size()
        sleep(2)
        x1 = swipe_up[0] / 2
        y1 = swipe_up[1] / 10 * 9
        x = swipe_up[1] / 10
        swipe_up.swipe(x1, y1, x1, x)

    # 向下滑动
    def swipe_down(self):
        swipe_down = self.get_size()
        sleep(2)
        x1 = swipe_down[0] / 2
        y1 = swipe_down[1] / 10
        x = swipe_down[1] / 10 * 9
        swipe_down.swipe(x1, y1, x1, x)

    def Sliding_direction(self,direction):
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'life':
            self.swipe_life()
        elif direction == 'right':
            self.swipe_right()
        else:
            print("贾维斯：检查到你进输入的有误")

    # 获取屏幕大小
    def get_send(self,driver):
        send = driver.get_window_size()
        print(send)

    # 生成号码
    def generate_number(self):
        str_start = random.choice(['135', '136', '138','150','180','158','181'])  # 它会循环我添加的这几个列表值，每次循环不一样
        # sample从指令序列中随机获取指定长度的片段。sample函数不会修改原有的序列。8是保留8位
        str_end = ''.join(random.sample('0123456789', 8))
        str_phone = str_start + str_end
        return str_phone

    # 将生成的电话号码写入文件
    def os_path(self,fps):
        str_number = self.generate_number()
        print(str_number)
        cwd = fps
        print(cwd)
        fp = open(cwd, 'w', encoding='utf-8')
        fp.write(str_number)
        fp.close()
        return fp

    # 生成configparser文件实例
    def config_parser(self,username,password):
        config_url = '/Users/lw/django_1.11_lx/appium_app/config/LoalElement.ini'
        config = configparser.ConfigParser()
        config["login_element"] = {
                              'username': username,
                              'password': password,
                              }
        with open(config_url, 'w') as configfile:
            config.write(configfile)
        return config_url

    # csv获取某一列 （例如获取roomid的所有值）
    def get_csv_column(self,csv_url,column_title):
        """
        如果我们想用DictReader读取csv的某一列，就可以用列的标题查询：
        :param csv_url:
        :return:
        """
        with open(csv_url, 'r') as file:
            reader = csv.DictReader(file)
            column = [row[column_title] for row in reader]
            print(column)
        return column   # 将查询到的一列中所有的值返回

    # 获取所有数据
    def get_csv_whole(self,csv_url):
        """
        使用reader函数，接收一个可迭代的对象（比如csv文件），
        能返回一个生成器，就可以从其中解析出csv的内容：
        比如下面的代码可以读取csv的全部内容，以行为单位：
        :return:
        """
        with open(csv_url,'r') as csvfile:
            whole_obj = csv.reader(csvfile)
            row = [print(rows,"\n") for rows in whole_obj]
            print(row)
        return row  # 得到一个list对象    没有值时会返回一个None

    def md5_sign(self,sign_str,):
        md5 = hashlib.md5()  # 创建md5对象
        sign_str = sign_str # 要加密的对象
        sign_bytes_utf8 = sign_str.encode()  # 方法以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
        # update需要一个bytes格式参数
        md5.update(sign_bytes_utf8)  # 进行加密
        sign_md5 = md5.hexdigest()  # 该方法只接受byte类型，否则会报错
        print(sign_md5)
        return sign_md5



if __name__ == '__main__':
    df = Boot_file_Configuration()
