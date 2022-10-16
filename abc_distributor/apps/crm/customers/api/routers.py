from email.mime import base
from rest_framework.routers import DefaultRouter

from apps.crm.customers.api.viewsets.general_view import DistrictViewSet

router = DefaultRouter()

router.register(r'districts', DistrictViewSet, basename='districts')

urlpatterns = router.urls