import locustio
from locust import HttpLocust, TaskSet, task
import time, random, json, hashlib, requests, threading, sys
import queue
# 签名相关工具类
class Tool():
      pass

class UserBehavior(TaskSet):
    def on_start(self):
        """任务开始准备工作:只登录一次"""
        self.tool = Tool()
        self.token_single = self.tool.user_login('18666111000',env='prod')

    # 获取会员信息
    # @task()
    def getMember(self):
        try:
            token = self.locust.token_queue.get()
        except queue.Empty:
            print('token run out, test ended.')
            exit(0)
        # 请求数据模板
        example = dict(headers={'Content-Type': 'application/json', 'env': 'prod',
                                'token': token},
                       url='http://test.cn/wxmp/mall/member/getMember', method='GET', verify=False)
        # 对请求数据模板签名
        url = self.tool.get_sign(example)
        # 发送请求
        res = self.client.get(url,headers=example['headers']).json()
        # 把用完的token放回队列
        self.locust.token_queue.put_nowait(token)

# 虚拟用户类
class WebsiteUser(HttpLocust):
    task_set = UserBehavior # 置顶用户类的行为
    tool = Tool()
    token_list = tool.get_token_list()
    token_queue = queue.Queue()
    for token in token_list:
        token_queue.put_nowait(token)

    min_wait = 0
    max_wait = 0


# 命令行单机模式启动 locust.py 可以随意命名
# locust -f locust.py --host=https://test.com

# 命令行分布式模式启动
# locust -f locust.py --host=https://test.com --master
# locust -f locust.py --host=https://test.com --slave --master-host=192.168.24.131

# 非web模式,执行60秒,每秒增加200个用户.直到1000个用户 -c1000 -r 200 --run-time 60
# locust -f main.py -H http://test.cn --csv=report --no-web -c1000 -r 200 --run-time 60
# 在Pycharm中启动
if __name__ == "__main__":
    import os
    os.system("locust -f locust.py --host=https://test.com")