from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-crm/', include('apps.crm.customers.api.routers')),
    path('api-warehouse/', include('apps.warehouse.products.api.routers')),
    path('api-sales/', include('apps.sales.orders.api.routers')),
]
