# coding: utf-8
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'


class ProfileA(models.Model):
    user = models.ForeignKey(User)
    age = models.IntegerField(db_index=True)

    class Meta:
        db_table = 'profile_a'


class ProfileB(models.Model):
    user = models.ForeignKey(User)
    point = models.IntegerField(default=0)

    class Meta:
        db_table = 'profile_b'


class Player(object):
    def __init__(self):
        self.age = None

    def get_generation(self):
        if self.age:
            return u"%d代" % ((self.age / 10) * 10)
    generation = property(get_generation)

    def get_level(self):
        return self.point / 100
    level = property(get_level)
