# coding: utf-8
from datetime import datetime

from django.db import models


class DatedModel(models.Model):
    """
    日付が付けたモデル
    """
    ctime = models.DateTimeField(u'作成日時', default=datetime.now, db_index=True)
    utime = models.DateTimeField(u'更新日時', auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-ctime']
