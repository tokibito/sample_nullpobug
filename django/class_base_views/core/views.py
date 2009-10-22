# coding:utf8
from django.http import Http404

class ClassBaseViews(object):
    """
    クラスベースのビュー
    以下のようなビューを簡単に作れます。
    http://example.com/?action=アクション名
    挙動をいろいろ変えたい場合は、ClassBaseViewsを
    継承して__call__などをオーバーライドするとよいかも。
    """
    def __init__(self):
        self.views = {}

    def __call__(self, request, *args, **kwargs):
        action = request.GET.get('action', '')
        if action in self.views:
            return self.views[action](request, *args, **kwargs)
        raise Http404

    def register(self, view, name=''):
        self.views[name] = view

base_views = ClassBaseViews()
