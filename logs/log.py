import logging.config
import os

from appium.webdriver import webdriver

CON_LOG='pages.conf'
os.path.join(os.path.dirname(os.path.abspath(__file__)),'logs.conf')
logging.config.fileConfig(CON_LOG)
loggin = logging.getLogger()

loggin.info("贾维斯：\t>>>  info类型的日志")
loggin.error("贾维斯：\t>>>  error类型的日志")


