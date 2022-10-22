from apps.crm.customers.models import CustomerCategory, District
from rest_framework import serializers


class DistrictSerializer(serializers.ModelSerializer):
    '''
        Class to convert a District object to a JSON format.
    '''
    class Meta:
        model = District
        # indicates a subset of the default fields to be used in a model serializer
        exclude = ('created_at', 'updated_at',)

class CustomerCategorySerializer(serializers.ModelSerializer):
    '''
        Class to convert a Customer Category object to a JSON format.
    '''
    class Meta:
        model = CustomerCategory
        # indicates a subset of the default fields to be used in a model serializer
        exclude = ('created_at', 'updated_at',)