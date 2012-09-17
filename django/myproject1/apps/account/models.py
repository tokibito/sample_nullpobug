# coding: utf-8
from django.db import models

from newauth import api as newauth_api

from apps.common.models import DatedModel


class User(DatedModel, newauth_api.UserBase):
    """ユーザー
    """
    username = models.CharField(u'ユーザー名', max_length=40, unique=True, db_index=True)
    password = models.CharField(u'パスワード', max_length=32)

    def __unicode__(self):
        return '%s' % self.username

    class Meta:
        db_table = 'user'
        verbose_name = u'ユーザー'
        verbose_name_plural = verbose_name


class AnonymousUser(newauth_api.AnonymousUserBase):
    pass
