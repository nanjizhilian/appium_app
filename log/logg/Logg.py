import logging
import os.path
import time


class Log(object):

    def __init__(self, log):
        # 创建一个log
        # getLogger(log)中log为日志记录的模块名字，后面的日志格式中的 %(name)s对应的是这里的模块名字
        self.log = logging.getLogger(log)
        # 设置日志级别，高于DEBUG的才会显示
        self.log.setLevel(logging.DEBUG)

        '''创建handler'''

        # 获取项目根目录的相对路径
        log_path = "/Users/liuwei/python_project/pyhon_testing/appium_app/log/logg/"
        # log_path = os.path.dirname(os.path.abspath('.')) + '/logg/'
        # log_path = os.getcwd()
        log_name = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        print(log_name)

        # 创建一个handler,用来写日志文件
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.log.addHandler(fh)
        self.log.addHandler(ch)

    def getlog(self):
        return self.log




