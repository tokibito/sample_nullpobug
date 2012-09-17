from django.conf.urls import patterns, include, url

from apps.note import views as note_views


urlpatterns = patterns('',
    url(r'^create$', note_views.NoteCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit$', note_views.NoteUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/json$', note_views.NoteJsonView.as_view(), name='json'),
    url(r'^(?P<pk>\d+)/$', note_views.NoteDetailView.as_view(), name='detail'),
)
