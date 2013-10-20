# coding: utf-8
from tastypie.resources import ModelResource
from myapp.models import Item
from myapp.mappers import ItemMapper

class ItemResource(ModelResource):
    def dehydrate(self, bundle):
        # Bundleオブジェクトのdata辞書をbpmappersでマッピングする
        # モデルのフィールドとresource_uriという名前のキーがbundle.dataに入ってる
        # ここでrequestオブジェクトを使いたい場合はbundle.requestを参照すればよい
        bundle.data = ItemMapper(bundle.data).as_dict()
        return bundle

    class Meta:
        queryset = Item.objects.all()
        allowed_methods = ['get']
