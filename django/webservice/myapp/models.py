from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
