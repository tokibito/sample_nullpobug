# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from myapp.views import MyView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', MyView.as_view()),
)
