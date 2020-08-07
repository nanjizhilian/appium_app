import os
from time import strftime
import logging


class Log:
    def __init__(self, logpath):
        self.now = strftime("%Y-%m-%d-%H")
        self.logname = os.path.join(logpath, '{0}.log'.format(self.now))

    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    # 日志分级之—debug
    def debug(self, message):
        self.__printconsole('debug', message)

    # 日志分级之—info
    def info(self, message):
        self.__printconsole('info', message)

    # 日志分级之—warning
    def warning(self, message):
        self.__printconsole('warning', message)

    # 日志分级之—error
    def error(self, message):
        self.__printconsole('error', message)


if __name__ == '__main__':
    path = "/Users/liuwei/python_project/pyhon_testing/appium_app/log/"
    Log(logpath=path).info(message="first log")
    # ret = os.getcwd()
    # print(ret)


