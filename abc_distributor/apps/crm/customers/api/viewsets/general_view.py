from rest_framework import viewsets

from apps.crm.customers.api.serializers.general_serializer import DistrictSerializer

class DistrictViewSet(viewsets.ModelViewSet):

    serializer_class = DistrictSerializer
    queryset = DistrictSerializer.Meta.model.objects.all()