# -*- coding: utf-8 -*-
import re
from django import http
from django.conf import settings
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template
from bookmarks.models import *
from bookmarks.views import *

class ItemNodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'ctime']
    list_filter = ['ctime']
    search_fields = ['name']

class ItemNodeInline(admin.StackedInline):
    model = ItemNode
    extra = 3

class CategoryAdmin(ItemNodeAdmin):
    inlines = [ItemNodeInline]

class MyAdmin(admin.AdminSite):
    index_template = 'my_index.html'

    def root(self, request, url):
        """
        Handles main URL routing for the admin app.

        `url` is the remainder of the URL -- e.g. 'comments/comment/'.
        """
        if request.method == 'GET' and not request.path.endswith('/'):
            return http.HttpResponseRedirect(request.path + '/')

        if settings.DEBUG:
            self.check_dependencies()

        # Figure out the admin base URL path and stash it for later use
        self.root_path = re.sub(re.escape(url) + '$', '', request.path)

        url = url.rstrip('/') # Trim trailing slash, if it exists.

        # The 'logout' view doesn't require that the person is logged in.
        if url == 'logout':
            return self.logout(request)

        # Check permission to continue or display login form.
        if not self.has_permission(request):
            return self.login(request)

        if url == '':
            return self.index(request)
        elif url == 'password_change':
            return self.password_change(request)
        elif url == 'password_change/done':
            return self.password_change_done(request)
        elif url == 'jsi18n':
            return self.i18n_javascript(request)

        # myadmin
        elif url == 'mybookmark':
            return self.bookmark_index(request)
        elif url == 'get_mybookmarks':
            return get_bookmarks(request)
        elif url == 'get_myfeeds':
            return get_feeds(request)
        # URLs starting with 'r/' are for the "View on site" links.
        elif url.startswith('r/'):
            from django.contrib.contenttypes.views import shortcut
            return shortcut(request, *url.split('/')[1:])
        else:
            if '/' in url:
                return self.model_page(request, *url.split('/', 2))
            else:
                return self.app_index(request, url)

        raise http.Http404('The requested admin page does not exist.')

    def login(self, request):
        return auth_views.login(request, 'admin/login.html')

    def bookmark_index(self, request):
        return direct_to_template(request, 'bookmark.html',
                extra_context={
                    'title': u'ブックマーク'
                })


    #def has_permission(self, request):
    #    return True # Trueを返すと管理サイトを表示可能

myadmin = MyAdmin()
myadmin.register([Site, Group, User, Bookmark, Feed])
myadmin.register(Category, CategoryAdmin)
myadmin.register(ItemNode, ItemNodeAdmin)

#admin.site.register([ItemNode, Bookmark, Category])
#admin.site.index_template = 'my_index.html'

#admin_bookmark = admin.AdminSite()
#admin_bookmark.register(Bookmark)
#admin_bookmark.register(Category)
