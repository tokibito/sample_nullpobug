# coding: utf-8
from django.views.generic import CreateView
from django.core.urlresolvers import reverse

from guestbook.models import Greeting
from guestbook.forms import GreetingForm


class IndexView(CreateView):
    u"""
    テンプレートによるフォーム表示と
    送信されたフォーム内容をモデルに保存する
    クラスベース汎用ビューを使用
    """
    model = Greeting
    form_class = GreetingForm

    def get_success_url(self):
        return reverse('guestbook:index')

    def get_context_data(self, **kwargs):
        context = kwargs
        context['greeting_list'] = Greeting.objects.all()
        return context
