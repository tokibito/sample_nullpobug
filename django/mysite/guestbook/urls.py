# coding: utf-8
from django.conf.urls import patterns, url, include

from guestbook.views import GreetingCreateView


urlpatterns = patterns('',
    url(r'^$', GreetingCreateView.as_view(), name='guestbook_index'),
)
