import json
import requests


class HttpRequests(object):

     def __init__(self):
         self.session = requests.Session()

     def send_request(self, method, url, params_type='form', data=None, **kwargs):
         method = method.upper()
         params_type = params_type.upper()
         if isinstance(data, str):
             try:
                 data = json.loads(data)
             except Exception:
                     data = eval(data)
         if 'GET' == method:
             response = self.session.request(method=method, url=url, params=data, **kwargs)
         elif 'POST' == method:

             # 发送表单数据，使用data参数传递
             if params_type == 'FORM':
                 response = self.session.request(method=method, url=url, data=data, **kwargs)

             # 如果接口支持application/json类型，则使用json参数传递
             elif params_type == 'JSON':
                 response = self.session.request(method=method, url=url, json=data, **kwargs)

             # 如果接口需要传递其他类型的数据比如 上传文件，调用下面的请求方法
             else:
                 response = self.session.request(method=method, url=url, **kwargs)

         # 如果请求方式非 get 和post 会报错，当然你也可以继续添加其他的请求方法
         else:
             raise ValueError('request method "{}" error ! please check'.format(method))
         return response

     def __call__(self, method, url, params_type='form', data=None, **kwargs):
         return self.send_request(method, url,
                                  params_type=params_type,
                                  data=data,
                                  **kwargs)

     def close_session(self):

         self.session.close()

         try:
             del self.session.cookies['JSESSIONID']

         except:
             pass


class RunMain:

    def send_post(self, url, data, headers):  # 定义一个方法，传入需要的参数url和data
        result = requests.request("POST", url, data=data, headers=headers)
        return result
        # print res

    def send_get(self, url, data):
        result = requests.get(url=url, data=data)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None, headers=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data, headers)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("错误")
        return result


request = HttpRequests()


if __name__ == '__main__':
    pass


