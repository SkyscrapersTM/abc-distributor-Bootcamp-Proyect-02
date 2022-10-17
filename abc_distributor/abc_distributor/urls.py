from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-crm/', include('apps.crm.customers.api.routers')),
    path('api-warehouse/', include('apps.warehouse.products.api.routers')),
]
