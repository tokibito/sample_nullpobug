from django.conf.urls import patterns, include, url
from django.shortcuts import render

from apps.webpage.views import HomeView


urlpatterns = patterns('',
    url(r'^$', render, {'template_name': 'index.html'}, name='top'),
    url(r'^home$', HomeView.as_view(), name='home'),
)
