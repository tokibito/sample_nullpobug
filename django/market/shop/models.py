# coding: utf-8
from django.db import models

class Category(models.Model):
    "カテゴリ"
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'category'

class Item(models.Model):
    "商品"
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=10, unique=True)
    price = models.IntegerField()
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'item'

class Bundle(models.Model):
    "まとめ売り"
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    items = models.ManyToManyField('Item', through='BundleItem')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'bundle'

class BundleItem(models.Model):
    "まとめ売り商品"
    bundle = models.ForeignKey('Bundle')
    item = models.ForeignKey('Item')

    class Meta:
        db_table = 'bundle_item'
