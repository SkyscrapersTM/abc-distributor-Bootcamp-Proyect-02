from django.contrib import admin

from apps.sales.orders.models import DetailOrder, Order

# register the models to the admin panel

admin.site.register(DetailOrder)
admin.site.register(Order)