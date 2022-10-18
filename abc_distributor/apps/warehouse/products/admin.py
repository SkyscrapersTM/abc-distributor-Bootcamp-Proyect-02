from django.contrib import admin
from apps.warehouse.products.models import UnitMeasureCategory
from apps.warehouse.products.models import UnitMeasure
from apps.warehouse.products.models import ProductCategory
from apps.warehouse.products.models import Product

admin.site.register(UnitMeasureCategory)
admin.site.register(UnitMeasure)
admin.site.register(ProductCategory)
admin.site.register(Product)
