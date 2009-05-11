# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#from bookmarks.admin import admin_bookmark
from bookmarks.admin import myadmin
#from django.contrib.auth.decorators import login_required

#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^hogeadmin/', include('hogeadmin.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    (r'^admin/bookmarks/(.*)', admin_bookmark.root), # これをやると /admin/ のリンクがおかしくなる
#    (r'^admin/(.*)', admin.site.root),
    (r'^admin/(.*)', myadmin.root),
)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)', serve,
        {'document_root': settings.MEDIA_ROOT}),
    )