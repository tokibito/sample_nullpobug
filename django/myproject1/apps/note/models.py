# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse as url_reverse

from apps.common.models import DatedModel


class Note(DatedModel):
    """ノート
    """
    title = models.CharField(u'タイトル', max_length=40)
    text = models.TextField(u'テキスト')
    user = models.ForeignKey('account.User')

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return url_reverse('note:detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'note'
        verbose_name = u'ノート'
        verbose_name_plural = verbose_name
        ordering = ['-ctime']
