from django.template.loaders.base import Loader as BaseLoader
from django.template import Origin
from .models import Template

class DatabaseOrigin(Origin):
    def __init__(self, name, template_name=None, loader=None, object=None):
        super().__init__(name, template_name, loader)
        self.object = object


class Loader(BaseLoader):
    def get_contents(self, origin):
        return origin.object.source

    def get_template_sources(self, template_name):
        # データベースからテンプレートデータを取得
        template = Template.objects.filter(name=template_name).first()
        if not template:
            return []
        # テンプレートのデータをカスタムのOriginクラスでラップして返す。
        origin = DatabaseOrigin(
            name=template_name,
            template_name=template_name,
            loader=self,
            object=template)
        return [origin]