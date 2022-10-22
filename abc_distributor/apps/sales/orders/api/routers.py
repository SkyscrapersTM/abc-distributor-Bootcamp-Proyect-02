from rest_framework.routers import DefaultRouter

from apps.sales.orders.api.viewsets.order_views import OrderViewSet

'''
    REST framework adds support for automatic URL routing to Django, 
    and provides you with a simple,
    quick and consistent way of wiring your view logic to a set of URLs
    — Inspired by Ruby.
'''

router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = router.urls