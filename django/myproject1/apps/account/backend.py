# coding: utf-8
from newauth.backend import ModelAuthBackend

from apps.account import api as account_api


class UserBackend(ModelAuthBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = self.user_model.objects.get(username=username)
            if account_api.check_password(password, user.password):
                return user
        except self.user_model.DoesNotExist:
            pass
        return None
