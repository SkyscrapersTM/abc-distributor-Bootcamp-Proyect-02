from rest_framework import serializers

from apps.sales.orders.models import DetailOrder

class DetailOrderSerializer(serializers.Serializer):
    
    class Meta:

        model = DetailOrder
        fields = '__all__'
