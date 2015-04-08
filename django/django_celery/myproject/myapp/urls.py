from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.list_message, name='list_message'),
    url(r'^create_message', views.create_message, name='create_message'),
]
