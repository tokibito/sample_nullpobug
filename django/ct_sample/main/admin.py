from django.contrib import admin
from multicontents.models import SimpleMemoItem
from main.models import Event

admin.site.register([Event, SimpleMemoItem])
