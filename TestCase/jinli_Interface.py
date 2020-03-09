import HTMLTestRunner
import requests
import unittest
from Assertion.Assertion_test import ConfigParser_ini_obj


def cookie_index(keyword=None,pagenum=None,pagesize=None):
    session_data = {
        'appVersion': '1.1.0',
        'appVersionCode': 10,
        'channel': 'a03',
        'device': 2,
        'imei': "5ED71FCA82B714A0FF6AF1046DA3306F",
        'keyword': None,
        'osVersion': 9,
        'signstr': '2c4c7adce6c7e8625df7ff1c254983c1',
        'timestamp': 1580469982,
        'token': '5976e297087535d78380e0ab4fdd48e3',
        'userId': '412763635283267584',
        'pagenum': pagenum,   # 首页接口参数
        'pagesize':pagesize,  # 首页接口参数页数
    }
    return session_data


class get_search(unittest.TestCase):

    def setUp(self):
        print("初始case进入")
        # 主地址
        self.index_url = 'http://www.duxunkeji.com:8100/'
        # 首页栏目框获取首页接口
        self.home_index_column = 'v1/home/index/'
        self.index_home_column = self.index_url+self.home_index_column  # 首页的接口地址拼接

        # 首页搜索接口url
        self.url = 'http://www.duxunkeji.com:8100/v1/search/'

        # 魅力榜-日榜
        self.charm_day = 'v1/rank/charm/day'
        self.index_charm_daya = self.index_url+self.charm_day

        # 魅力榜-月榜
        self.rank_charm_month = 'v1/rank/charm/month'
        self.charm_month = self.index_url+self.rank_charm_month



        # cookie信息
        self.cookie_index = cookie_index
        print("初始case结束")

    # ini文件
    def test_read_ini_ConfigParser_obj(self):
        read_ini = ConfigParser_ini_obj()
        return read_ini

    # 搜索接口
    def test_search(self,keyword=None):
        print("进入搜索接口")
        session_data={
            'appVersion': '1.1.0',
            'appVersionCode': 10,
            'channel': 'a03',
            'device': 2,
            'imei': "5ED71FCA82B714A0FF6AF1046DA3306F",
            'keyword': keyword,
            'osVersion': 9,
            'signstr': '2c4c7adce6c7e8625df7ff1c254983c1',
            'timestamp': 1580469982,
            'token': '5976e297087535d78380e0ab4fdd48e3',
            'userId': '412763635283267584',
        }
        response = requests.post(self.url, session_data)
        return response

    # 房间名搜索
    def test_home_index(self):
        key_word = self.test_read_ini_ConfigParser_obj()
        key_word.config_ini("index_key_word","key_word")
        response = self.test_search(key_word)
        num = response.json()
        print(num)
        print(type(response))

        code = response.status_code
        print("搜索结果状态吗为", code)

    # 空字符串
    def test_home_None(self):
        print("搜索接口空字符串测试---")
        Nene_key = self.test_read_ini_ConfigParser_obj()
        Nene_key.config_ini('index_key_word',"Nene_key")
        response = self.test_search(Nene_key)
        response = response.json()
        print(response)
        if response['code'] == 200:
            print("空字符返回正常")
        else:
            print("接口空字符串返回有误")

    # 首页栏目--获取内容接口
    def test_home_index_column(self):
        print("这是首页栏目--获取内容接口")
        ini_read = self.test_read_ini_ConfigParser_obj()
        pagenum = ini_read.config_ini('Home_page_interface','pagenum')
        pagesize = ini_read.config_ini('Home_page_interface','pagesize')
        response = requests.get(self.index_home_column,cookie_index(pagenum,pagesize))
        print(response.json())

    # # 首页栏目--获取内容接口-----
    def test_home_index_column_02(self):
        """
        传入参数大于当前页数和pagesize
        :return:
        """
        read_ini = ConfigParser_ini_obj()
        ini_pagenum = read_ini.config_ini('Home_page_interface','pagenum')
        ini_pagesize = read_ini.config_ini('Home_page_interface','pagesize')
        response = requests.get(self.index_home_column,cookie_index(ini_pagesize,ini_pagenum))
        print(response.json())
        if response.status_code == 200:
            print("接口返回正常")
        else:
            print("接口异常")

    # 首页栏目获取内容接口
    def test_home_index_colimn_03(self):
        """
        传入负数
        :return:
        """
        print("首页搜索传入负数")
        response = requests.get(self.index_home_column,self.cookie_index(-1,-10))
        ret = response.json()
        list = []
        for num in ret:
            num_code = num['code']
            num_message = num['message']
            num_success = num['success']
            num_list = {"code":num_code,"messgae":num_message,'success':num_success}
            list.append(num_list)

    def test_rank_charm_day_01(self,userId=None):
        """
        魅力榜---日榜
        :return:
        """
        session_data = {
            'userId': userId,
            'roomid':'422115210053160960'
        }
        response = requests.get(self.index_charm_daya,session_data)
        return response.json()

    def test_rank_charm_day_02(self):
        """
        测试榜单
        :return:
        """
        code = 200
        ini_obj = self.test_read_ini_ConfigParser_obj()
        userId = ini_obj.config_ini('Home_page_interface', 'userIDS')
        for num in self.test_rank_charm_day_01(userId):
            num_code = num['code']
            num_success = num['success']
            self.assertEqual(code,num_code,msg='魅力榜日榜状态（code）返回异常')
            self.assertTrue(num_success,msg='魅力榜日榜的success不是True')

    def test_rank_charm_day_03(self):
        """
        不存在的用户id
        :return:
        """
        ini_obj = self.test_read_ini_ConfigParser_obj()
        userId = ini_obj.config_ini('Home_page_interface','userIDS')
        rank = self.test_rank_charm_day_01(userId)
        print(rank)

    def test_rank_charm_month_01(self):
        """
        魅力榜月榜---正常请求
        :return:
        """
        print('*'*30)
        data = {
            'userId': '422105422690914304',
            'roomid': '422115210053160960'
        }
        resp = requests.get(self.charm_month,data)
        print(resp.json())
        self.assertTrue()
        print('='*30)



    # 最后执行
    def tearDown(self):
        print('the is tearDown')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(get_search('test_search'))
    # suite.addTest(get_search('test_home_index'))
    # suite.addTest(get_search('test_home_None'))
    # suite.addTest(get_search('test_home_index_column'))
    # suite.addTest(get_search('test_home_index_column_02'))
    # suite.addTest(get_search('test_home_index_colimn_03'))
    # suite.addTest(get_search('tearDown'))
    # suite.addTest(get_search('test_rank_charm_day_01'))
    # suite.addTest(get_search('test_rank_charm_day_02'))
    # suite.addTest(get_search('test_rank_charm_day_03'))
    suite.addTest(get_search('test_rank_charm_month_01'))
    html_file = "/Users/lw/django_1.11_lx/appium_app/report.html"
    fp = open(html_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况:')
    runner.run(suite)
    fp.close()


