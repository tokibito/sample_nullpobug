from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=255)
    source = models.TextField()

    def __str__(self):
        return f"{self.name}"