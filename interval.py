#from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler

import latest_all_stock_k_data
import datetime

def daily_job():
    specified_date=datetime.date.today().strftime('%Y-%m-%d')
    latest_all_stock_k_data.latest_all_stock_k_data(specified_date)

def tick():
    print('Tick! The time is: %s' % datetime.datetime.now())

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # 间隔3秒钟执行一次
    scheduler.add_job(daily_job, 'interval', minutes=30, start_date='2019-10-24 23:48:00',end_date='2019-11-24 21:35:00')
    # 这里的调度任务是独立的一个线程
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # 其他任务是独立的线程执行
        while True:
            time.sleep(15)
            print('.....')
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Exit The Job!')