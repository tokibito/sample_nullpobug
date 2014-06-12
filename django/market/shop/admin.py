from django.contrib import admin
from shop.models import Item, Bundle, Category, BundleItem

admin.site.register([Item, Bundle, Category, BundleItem])
