from django.apps import AppConfig


class CeleryConfig(AppConfig):
    name = 'celery_config'

    def ready(self):
        from myproject.celery_app import get_celery_app
        get_celery_app()
