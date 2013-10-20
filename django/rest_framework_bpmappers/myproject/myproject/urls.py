from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^items/', 'myapp.views.item_list'),
)
