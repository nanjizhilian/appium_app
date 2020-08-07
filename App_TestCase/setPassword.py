import unittest
from copy import copy
from Public_method.operatio_excel import OperationExcel
from Public_method.Get_excel_open import Get_Data
import requests
from Public_method.sign_test import sign


class setpassword(unittest.TestCase):
    def setUp(self):
        self.get_excel_data = Get_Data()
        self.sign = sign()
        self.wd_open = OperationExcel()

    def test_password(self):
        # self.get_excel_data.get_request_method(5)
        url = self.get_excel_data.get_request_url(5)
        data = self.get_excel_data.get_excel_data(5)
        header = self.get_excel_data.is_header(5)
        str_data = str(url,data,header)
        sign_str = sign(str_data)
        copy_data = self.get_excel_data.get_excel_data(5)
        copy(copy_data)
        self.wd_open.write_value(5,2,sign_str)

        reseponse = requests.post(url,data,header)
        print(reseponse.text)


if __name__ == '__main__':
    ret = setpassword()
    ret.test_password()





