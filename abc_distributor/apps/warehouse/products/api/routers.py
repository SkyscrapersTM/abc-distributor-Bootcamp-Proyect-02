from rest_framework.routers import DefaultRouter

from apps.warehouse.products.api.viewsets.general_view import ProductCategoryViewSet

router = DefaultRouter()

router.register(r'product-category', ProductCategoryViewSet, basename='product-category')

urlpatterns = router.urls