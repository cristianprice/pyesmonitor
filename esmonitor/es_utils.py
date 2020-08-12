from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


ES_STATS_TYPES = (('node_stats', 'node_stats'),
                  ('cluster_stats', 'cluster_stats'))


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

executors = {
    'default': ThreadPoolExecutor(20)
}

job_defaults = {
    'coalesce': True,
    'max_instances': 20
}


def print_ping():
    print('Ping: ', datetime.now())


scheduler = BackgroundScheduler()
scheduler.configure(jobstores=jobstores, executors=executors,
                    job_defaults=job_defaults)


def start():
    scheduler.add_job(print_ping, 'interval', seconds=5)
    scheduler.start()
