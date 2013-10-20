from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
