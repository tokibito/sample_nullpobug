from django.db import models


class Message(models.Model):
    body = models.CharField(max_length=100)

    def __str__(self):
        return "pk={}, body={}".format(self.pk, self.body)
