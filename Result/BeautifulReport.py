import time
import unittest

from Result import HTMLTestRunner


class TEST_HTML(unittest.TestCase):
    def setUp(self):
        """最先执行"""
        print("最先执行的测试用例")

    def test_demo1(self):
        """第一条用例"""
        print("第一条测试用例")

    @classmethod
    def test_demo2(cls):
        """魔法用例"""
        print("第二条测试用例：拥有魔法函数：classmethod")


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = "../util/" + now + "_result.html"
    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'搜索功能测试报告',
        description=u'用例执行情况：')

    runner.run(TEST_HTML())

    # 关闭文件流，不关的话生成的报告是空的
    fp.close()



