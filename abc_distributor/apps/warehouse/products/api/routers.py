from rest_framework.routers import DefaultRouter

from apps.warehouse.products.api.viewsets.general_view import ProductCategoryViewSet
from apps.warehouse.products.api.viewsets.products_views import ProductViewSet

'''
    REST framework adds support for automatic URL routing to Django, 
    and provides you with a simple,
    quick and consistent way of wiring your view logic to a set of URLs
    — Inspired by Ruby.
'''

router = DefaultRouter()

router.register(r'product-category', ProductCategoryViewSet,
                basename='product-category')

router.register(r'product', ProductViewSet, basename='product')

urlpatterns = router.urls
