# coding: utf8
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.create_update import create_object
from django.template import Template, RequestContext
from django.template.loader import render_to_string

from guestbook.models import Greeting
from guestbook.forms import GreetingForm

def index(request):
    # 汎用ビューを利用
    return create_object(request,
                         form_class=GreetingForm,
                         post_save_redirect=reverse('guestbook_index'),
                         extra_context={'greeting_list': Greeting.objects.all()})

def index2(request):
    # 汎用ビューをを使わない場合
    # フォームオブジェクトを作成して入力内容の検証
    form = GreetingForm(request.POST or None)
    if form.is_valid():
        # 内容を保存してリダイレクト
        form.save()
        return HttpResponseRedirect(reverse('guestbook_index'))
    # コンテキストを作成
    context = RequestContext(request)
    context['greeting_list'] = Greeting.objects.all()
    context['form'] = form
    # レンダリングしてページを表示
    return HttpResponse(render_to_string('guestbook/greeting_form.html', context))
