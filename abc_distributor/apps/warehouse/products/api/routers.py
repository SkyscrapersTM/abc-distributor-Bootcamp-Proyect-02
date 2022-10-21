from rest_framework.routers import DefaultRouter

from apps.warehouse.products.api.viewsets.general_view import ProductCategoryViewSet
from apps.warehouse.products.api.viewsets.products_views import ProductViewSet

router = DefaultRouter()

router.register(r'product-category', ProductCategoryViewSet,
                basename='product-category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = router.urls
