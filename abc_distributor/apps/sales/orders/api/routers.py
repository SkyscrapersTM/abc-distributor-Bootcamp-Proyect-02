from rest_framework.routers import DefaultRouter

from apps.sales.orders.api.viewsets.order_views import OrderViewSet

router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = router.urls