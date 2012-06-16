# coding: utf8
from django.contrib import admin

from guestbook.models import Greeting

class GreetingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'username', 'create_at')
    list_filter = ('create_at', 'username')
    search_fields = ('username', 'content')

# Adminサイトへ登録する
admin.site.register(Greeting, GreetingAdmin)
