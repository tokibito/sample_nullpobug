# coding: utf-8
from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(u'緯度', max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(u'経度', max_digits=9, decimal_places=6, default=0)

    class Meta:
        db_table = 'shop'

    def __unicode__(self):
        return self.name
