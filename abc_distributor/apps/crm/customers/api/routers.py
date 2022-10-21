from rest_framework.routers import DefaultRouter

from apps.crm.customers.api.viewsets.general_view import DistrictViewSet, CustomerCategoryViewSet
from apps.crm.customers.api.viewsets.customer_views import CustomerViewSet

router = DefaultRouter()

router.register(r'districts', DistrictViewSet, basename='districts')
router.register(r'customer-category', CustomerCategoryViewSet, basename='customer-category')
router.register(r'customers', CustomerViewSet, basename='customers')

urlpatterns = router.urls