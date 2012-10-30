from django.conf.urls import patterns, include, url
from myapp.views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
)
