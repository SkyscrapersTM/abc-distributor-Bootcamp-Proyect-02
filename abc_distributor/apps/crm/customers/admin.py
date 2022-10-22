from django.contrib import admin

from apps.crm.customers.models import District
from apps.crm.customers.models import CustomerCategory
from apps.crm.customers.models import Customer

# register the models to the admin panel

admin.site.register(District)
admin.site.register(CustomerCategory)
admin.site.register(Customer)
