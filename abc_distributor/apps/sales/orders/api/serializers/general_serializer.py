from rest_framework import serializers

from apps.sales.orders.models import DetailOrder

class DetailOrderSerializer(serializers.Serializer):
    '''
        Class to convert a Detail Order object to a JSON format.
    '''
    class Meta:

        model = DetailOrder
        fields = '__all__'
