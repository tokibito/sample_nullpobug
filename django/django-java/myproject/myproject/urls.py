from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'myapp.views.index', name='index'),
)
