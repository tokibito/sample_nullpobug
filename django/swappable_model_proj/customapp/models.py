from django.db import models
from baseapp.models import AbstractItem


class CustomItem(AbstractItem):
    """カスタマイズしたモデル
    """
    price = models.IntegerField()

    class Meta(AbstractItem.Meta):
        db_table = 'custom_item'

    def display(self):
        return "{}: {}".format(self.name, self.price)
