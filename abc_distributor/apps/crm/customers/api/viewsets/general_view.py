from rest_framework import viewsets

from apps.crm.customers.api.serializers.general_serializer import DistrictSerializer, CustomerCategorySerializer


class DistrictViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides the standard actions
        https://www.django-rest-framework.org/api-guide/viewsets/
    """
    serializer_class = DistrictSerializer
    queryset = DistrictSerializer.Meta.model.objects.all()


class CustomerCategoryViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides the standard actions
        https://www.django-rest-framework.org/api-guide/viewsets/
    """
    serializer_class = CustomerCategorySerializer
    queryset = CustomerCategorySerializer.Meta.model.objects.all()
