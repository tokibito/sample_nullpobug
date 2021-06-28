# coding: utf-8
from datetime import datetime

from django.db import models


class Greeting(models.Model):
    """
    ゲストブックのコンテンツのモデル
    """
    username = models.CharField(u'名前', max_length=30)
    content = models.TextField(u'書き込み内容', max_length=1000)
    create_at = models.DateTimeField(u'書き込み日時', default=datetime.now)

    def __unicode__(self):
        """
        モデルの文字列表現
        内容の改行を削除して先頭から20文字を返す
        """
        return ''.join(unicode(self.content).splitlines())[:20]

    class Meta:
        # ソート順
        ordering = ('-create_at',)
        # 単数形
        verbose_name = u'書き込み'
        # 複数形
        verbose_name_plural = u'書き込み'


class Note(models.Model):
    """ ノート

    https://tracery.jp/s/a47b8269bc7c46e4a9a64bbdc0374050

    ページを束ねるノート
    """

    title = models.CharField(verbose_name="タイトル", null=True)
    created_at = models.DateTimeField(verbose_name="作成日時")

    class Meta:
        verbose_name = "ノート"
        db_table = "note"


class Page(models.Model):
    """ ページ

    https://tracery.jp/s/c9856202d66642f2829d4493afbfab08
    """

    number = models.IntegerField(verbose_name="ページ番号", default=1)
    body = models.TextField(verbose_name="本文", null=True)
    note = models.ForeignKey("Note", on_delete=models.DO_NOTHING, verbose_name="ノート")

    class Meta:
        verbose_name = "ページ"
        db_table = "page"
