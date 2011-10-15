# coding: utf-8
from django.db import models


class GroupManager(models.Manager):
    def private_groups(self):
        "非公開グループのみを返す"
        return self.get_query_set().filter(is_private=True)


class Permission(models.Model):
    name = models.CharField(u'権限名', max_length=16, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'権限'
        verbose_name_plural = verbose_name


class Group(models.Model):
    name = models.CharField(u'グループ名', max_length=16)
    permissions = models.ManyToManyField(Permission, verbose_name=u'所持権限')
    is_private = models.BooleanField(u'非公開')

    objects = GroupManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'グループ'
        verbose_name_plural = verbose_name


class User(models.Model):
    user_id = models.CharField(u'ユーザーID', max_length=16)
    email = models.EmailField(u'メールアドレス')
    groups = models.ManyToManyField(Group, verbose_name=u'所属グループ')

    def __unicode__(self):
        return self.user_id

    class Meta:
        verbose_name = u'グループ'
        verbose_name_plural = verbose_name
