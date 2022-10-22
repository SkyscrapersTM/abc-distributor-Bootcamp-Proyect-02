from django.contrib import admin

from apps.sales.currency.models import Currency

# register the model to the admin panel
admin.site.register(Currency)
