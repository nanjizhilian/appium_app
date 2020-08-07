import time
from apscheduler.schedulers.blocking import BlockingScheduler
from App_TestCase.app_test_id import login



def test_job():
    ojb = login()
    ojb.get_code()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
scheduler = BlockingScheduler()
scheduler.add_job(test_job, 'interval', seconds=5, id='test_job')
scheduler.start()
print("--------",scheduler.get_job('test_job'))

if __name__ == '__main__':
    test_job()


