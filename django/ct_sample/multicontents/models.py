# coding: utf-8
import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string

class MultiContentItem(models.Model):
    name = models.CharField(u'名前', max_length=100)
    create_at = models.DateTimeField(u'作成日時', default=datetime.datetime.now)
    update_at = models.DateTimeField(u'更新日時', default=datetime.datetime.now, auto_now=True)
    content_type = models.ForeignKey(ContentType, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # content_typeを上書きする
        self.content_type = ContentType.objects.get_for_model(self.__class__)
        super(MultiContentItem, self).save(*args, **kwargs)

    def _get_original(self):
        """
        ContentTypeに関連付けられたオブジェクトを取得する
        """
        try:
            return self.content_type.get_object_for_this_type()
        except models.ObjectDoesNotExist:
            return
    original = property(_get_original)

    def _get_template_name(self):
        """
        テンプレート名を取得する
        """
        try:
            return 'multicontents/_%s.html' % self.content_type.model
        except models.ObjectDoesNotExist:
            return
    template_name = property(_get_template_name)

    display_object_name = 'item'
    def display(self, context={}):
        """
        表示用
        """
        context[self.display_object_name] = self
        if self.template_name:
            return render_to_string(self.template_name, context)
        else:
            return ''

    class Meta:
        ordering = ('-create_at',)

class SimpleMemoItem(MultiContentItem):
    """
    テキストのみのシンプルなメモ
    """
    content = models.TextField(u'内容')
