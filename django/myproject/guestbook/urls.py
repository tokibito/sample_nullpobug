from django.conf.urls.defaults import patterns, url

from guestbook import views as guestbook_views


urlpatterns = patterns(
    '',
    url(r'^$', guestbook_views.IndexView.as_view(), name='index'),
)
