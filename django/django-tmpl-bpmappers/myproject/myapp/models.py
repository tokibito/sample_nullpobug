# coding: utf-8
from django.db import models


class A(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class B(models.Model):
    name = models.CharField(max_length=10)
    a = models.ForeignKey(A, null=True, blank=True)

    def __unicode__(self):
        return self.name


class C(models.Model):
    name = models.CharField(max_length=10)
    b_list = models.ManyToManyField(B, blank=True)

    def __unicode__(self):
        return self.name
