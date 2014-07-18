from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^no_prefetch$', 'shop.views.no_prefetch_view'),
    (r'^prefetch$', 'shop.views.prefetch_view'),

    url(r'^admin/', include(admin.site.urls)),
)
