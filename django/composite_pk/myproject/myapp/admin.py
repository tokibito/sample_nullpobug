from django.contrib import admin

from .models import Product, Order, OrderLineItem

admin.site.register(Product)
admin.site.register(Order)
OrderLineItem._meta.__class__.is_composite_pk = False
admin.site.register(OrderLineItem)
OrderLineItem._meta.__class__.is_composite_pk = True
