from crontab import CronTab
import os

my_cron = CronTab(user=True)


def start():
    job = my_cron.new(command='python3 '+os.path.dirname(os.path.realpath(__file__))+'/news_crawler.py', comment='webcrawlpythonapp')
    job.minute.every(15)
    my_cron.write()


def stop():
    for job in my_cron:
        if job.comment == 'webcrawlpythonapp':
            my_cron.remove(job)
            my_cron.write()
