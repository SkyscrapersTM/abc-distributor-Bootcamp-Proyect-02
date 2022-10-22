from rest_framework.routers import DefaultRouter

from apps.crm.customers.api.viewsets.general_view import DistrictViewSet, CustomerCategoryViewSet
from apps.crm.customers.api.viewsets.customer_views import CustomerViewSet

'''
    REST framework adds support for automatic URL routing to Django, 
    and provides you with a simple,
    quick and consistent way of wiring your view logic to a set of URLs
    — Inspired by Ruby.
'''

router = DefaultRouter()

router.register(r'districts', DistrictViewSet, basename='districts')
router.register(r'customer-category', CustomerCategoryViewSet, basename='customer-category')
router.register(r'customers', CustomerViewSet, basename='customers')

urlpatterns = router.urls