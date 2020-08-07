import json
import unittest
from Public_method.request_method import RunMain
from Public_method.Get_excel_open import Get_Data
from Public_method.operatio_excel import OperationExcel


class X_project(unittest.TestCase):

    def setUp(self):
        self.excel_data = Get_Data()
        self.run = RunMain()
        self.oper_excel = OperationExcel()

    def test_01(self):
        try:
            excel_data = self.excel_data.get_excel_data(1)
            excel_url = self.excel_data.get_request_url(1)
            print(excel_url)
            response = self.run.run_main("get", excel_url, excel_data)
            print(response.content)
        except Exception as f:
            print("发生异常",f)

        finally:
            print("程序执行完毕")


if __name__ == '__main__':
    obj = X_project()
    obj.test_01()





