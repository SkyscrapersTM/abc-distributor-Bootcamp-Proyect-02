from django.contrib import admin
from apps.warehouse.products.models import UnitMeasureCategory
from apps.warehouse.products.models import UnitMeasure

admin.site.register(UnitMeasureCategory)
admin.site.register(UnitMeasure)
