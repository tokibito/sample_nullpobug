from django.db import models


class AbstractItem(models.Model):
    """抽象モデル
    """
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Item(AbstractItem):
    """syncdb対象となるモデル
    差し替え可能とする
    """
    class Meta(AbstractItem.Meta):
        swappable = 'BASEAPP_ITEM_MODEL'
        db_table = 'item'

    def display(self):
        return self.name


def get_item_model():
    """Itemモデルクラスを取得する関数
    """
    from django.conf import settings
    app_label, model_name = settings.BASEAPP_ITEM_MODEL.split('.')
    item_model = models.get_model(app_label, model_name)
    return item_model


def print_all_items():
    """Itemモデルのデータを取得して画面に表示する関数
    """
    item_model = get_item_model()
    for item in item_model.objects.all():
        print(item.display())
