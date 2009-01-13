from django.contrib import admin
from multicontents.models import SimpleMemoItem
from main.models import Event, DownloadItem

admin.site.register([Event, DownloadItem, SimpleMemoItem])
