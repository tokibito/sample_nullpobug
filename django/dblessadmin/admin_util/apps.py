from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in


class AdminUtilConfig(AppConfig):
    name = 'admin_util'

    def ready(self):
        user_logged_in.disconnect(dispatch_uid='update_last_login')
