from django.contrib import admin

from myapp.models import A, B, C


admin.site.register([A, B, C])
