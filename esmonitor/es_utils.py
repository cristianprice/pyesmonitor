from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.interval import IntervalTrigger
from .es_http_utils import poll_stats
import logging
import coloredlogs
import json

coloredlogs.install()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

executors = {
    'default': ThreadPoolExecutor(30)
}

job_defaults = {
    'coalesce': True,
    'max_instances': 20
}


def print_ping():
    print('Ping: ', datetime.now())


def poll_es_stats(cluster_host, stat_type):
    from .models import ClusterHost, ES_STATS_TYPES, Stats

    json_content = poll_stats(
        cluster_host.host, cluster_host.port, cluster_host.protocol)

    Stats.objects.create(cluster_host=cluster_host,
                         name=stat_type, json_content=json.dumps(json_content))


scheduler = BackgroundScheduler()
scheduler.configure(jobstores=jobstores, executors=executors,
                    job_defaults=job_defaults)


def start():
    try:
        from .models import ClusterHost, ES_STATS_TYPES

        cluster_hosts = ClusterHost.objects.all()
        for cluster_host in cluster_hosts:

            host = cluster_host.host
            port = cluster_host.port
            scheduler.add_job(poll_es_stats, trigger=IntervalTrigger(seconds=15),
                              args=(cluster_host, ES_STATS_TYPES[0][0]),
                              id=f'{host}',
                              replace_existing=True)

        scheduler.start()
    except Exception as e:
        logger.warn('Failed to start scheduler.')
