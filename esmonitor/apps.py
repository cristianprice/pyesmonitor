from django.apps import AppConfig
from .es_utils import start


class EsmonitorConfig(AppConfig):
    name = 'esmonitor'

    def ready(self):
        start()
