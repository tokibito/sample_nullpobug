from django.apps import AppConfig
from base.signals import spam_main
from .egg import receiver


class App2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app2'

    def ready(self):
        spam_main.connect(receiver)
