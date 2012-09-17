from django.conf.urls import patterns, include, url

from newauth import views as newauth_views

from apps.account import views as account_views

urlpatterns = patterns('',
    url(r'^login$', newauth_views.login, {'template_name': 'account/login.html', 'next_page': 'webpage:home'}, name='login'),
    url(r'^logout$', newauth_views.logout, {'next_page': 'webpage:top'}, name='logout'),
)
