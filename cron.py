import time as tm
import schedule
from main import send_emails_using_data, df


def job():
    send_emails_using_data(df)


schedule.every(60).seconds.do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)


'''scheduler = BackgroundScheduler(timezone='Asia/Kolkata')
scheduler.start()

job = scheduler.add_job(send_emails_using_data, 'cron', args=[df], hour='18', minute='14')
print(job)

while True:
    time.sleep(1)
'''
