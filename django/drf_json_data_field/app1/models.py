from django.db import models


class Model1(models.Model):
    class Meta:
        ordering = ['pk']

    data = models.TextField("JSONデータ", null=True, blank=True)
