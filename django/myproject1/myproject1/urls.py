from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('apps.account.urls', 'account')),
    url(r'^note/', include('apps.note.urls', 'note')),
    url(r'', include('apps.webpage.urls', 'webpage')),
)
