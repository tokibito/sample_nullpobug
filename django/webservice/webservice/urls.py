from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^foo_service/$', 'foo_service.service.hello_app'),

    url(r'^admin/', include(admin.site.urls)),
)
