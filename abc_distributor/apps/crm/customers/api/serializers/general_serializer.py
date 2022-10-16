from apps.crm.customers.models import CustomerCategory, District
from rest_framework import serializers


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        exclude = ('created_at', 'updated_at',)
