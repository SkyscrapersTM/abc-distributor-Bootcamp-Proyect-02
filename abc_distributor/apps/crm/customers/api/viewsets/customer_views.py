from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.crm.customers.models import Customer

from apps.crm.customers.api.serializers.customer_serializer import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides the standard actions
    """
    queryset = CustomerSerializer.Meta.model.objects.all()
    serializer_class = CustomerSerializer

    # Create a custom viewset
    @action(detail=False, methods=['get'], url_path='filter-by-ruc')
    def filter_by_ruc(self, request, pk=None):
        '''
            This viewset filter customer by ruc paramater
        '''

        # get query parameter from the request
        param_ruc = request.query_params.get('ruc')

        # returns a single object that matches the given lookup parameter.
        customer = Customer.objects.get(ruc=param_ruc)

        # allow customer object to become JSON
        serializer = CustomerSerializer(customer)

        # display customer data for the response
        return Response(serializer.data, status=status.HTTP_200_OK)
