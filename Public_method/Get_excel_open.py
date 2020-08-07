import json

from Public_method import Excel_method
from Public_method.operatio_excel import OperationExcel
from Public_method.operation_json import OperetionJson


class Get_Data:
	def __init__(self):
		self.opera_excel = OperationExcel()
		self.returnNone = '暂无数据哦～～～'

	# 去获取excel行数, 就是我们的case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(Excel_method.get_run())
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#是否携带header
	def is_header(self,row):
		col = int(Excel_method.get_hander())
		header = self.opera_excel.get_cell_value(row,col)
		if header != '':
			return header
		else:
			return self.returnNone

	#获取请求方式
	def get_request_method(self,row):
		col = int(Excel_method.get_request_method())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取url
	def get_request_url(self,row):
		col = int(Excel_method.get_url())
		url = self.opera_excel.get_cell_value(row,col)
		return json.dumps(url, ensure_ascii=False)

	#获取请求数据
	def get_request_data(self,row):
		col = int(Excel_method.get_data())
		data = self.opera_excel.get_cell_value(row,col)
		if data == '':
			return self.returnNone
		return data

	#通过获取关键字拿到json文件中的data数据
	def get_data_for_json(self,row):
		opera_json = OperetionJson()
		request_data = opera_json.get_data(self.get_request_data(row))
		return request_data

	# 获取请求数据（excel中的data）
	def get_excel_data(self,row):
		col = int(Excel_method.get_data())
		excel_data = self.opera_excel.get_cell_value(row,col)
		if excel_data == '':
			print("数据为空")
			return self.returnNone
		return json.loads(excel_data)

	#获取预期结果
	def get_expcet_data(self,row):
		col = int(Excel_method.get_expect())
		expect = self.opera_excel.get_cell_value(row,col)
		if expect == '':
			return self.returnNone
		return expect

	#获取数据依赖字段
	def get_depend_field(self,row):
		col = int(Excel_method.get_field_depend())
		data = self.opera_excel.get_cell_value(row,col)
		if data == "":
			return self.returnNone
		else:
			return data

	# 写入返回结果
	def wriReturn(self, rowNum, value):
		colNum = int(Excel_method.getReturnResult())
		self.opera_excel.write_value(rowNum, colNum, value)


if __name__ == '__main__':
	obj = Get_Data()
	ret = obj.get_excel_data(4)
	print(ret)


