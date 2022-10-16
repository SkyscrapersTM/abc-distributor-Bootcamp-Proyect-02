from rest_framework import viewsets

from apps.crm.customers.api.serializers.customer_serializer import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer
    queryset = CustomerSerializer.Meta.model.objects.all()
