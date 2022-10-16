from django.contrib import admin

from apps.crm.customers.models import District
from apps.crm.customers.models import CustomerCategory
from apps.crm.customers.models import Customer

admin.site.register(District)
admin.site.register(CustomerCategory)
admin.site.register(Customer)
