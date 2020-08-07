class global_var:
	Id = '0'
	modular = '1'
	request_method = '2'
	url = '3'
	request_mustpass = '4'
	data = '5'
	run = '6'
	hander = '7'
	returnData = '8'
	field_depend = '9'
	expect = '10'
	result = '11'
#获取caseid
def get_id():
	return global_var.Id

#获取功能模块
def get_modular():
	return global_var.modular

# 获取请求方法
def get_request_method():
	return global_var.request_method

# 获取请求url
def get_url():
	return global_var.url

# 请求通过
def get_request_mustpass():
	return global_var.request_mustpass

# 请求数据
def get_data():
	return global_var.data

# 是否运行
def get_run():
	return global_var.run

# hander
def get_hander():
	return global_var.hander

#  预期结果
def get_expect():
	return global_var.expect

# 实际结果
def get_result():
	return global_var.result

# 是否有依赖字段
def get_field_depend():
	return global_var.field_depend

#获取返回数据
def getReturnResult():
	return global_var.returnData
