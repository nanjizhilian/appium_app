import configparser


class ReadIni():
    def __init__(self,file_path=None):
        # 查看是否有此配置文件
        if file_path == None:
            self.file_path = '/Users/lw/django_1.11_lx/appium_app/config/LoalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    # 读取配置文件的路径
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    # 读取配置文件内容
    def get_values(self,key,secsion=None):

        if secsion == None:

            secsion = 'login_element'

        try:
            value = self.data.get(secsion,key)
        except:
            value = None
        return value

