from django.contrib import admin

from apps.sales.orders.models import DetailOrder, Order

admin.site.register(DetailOrder)
admin.site.register(Order)