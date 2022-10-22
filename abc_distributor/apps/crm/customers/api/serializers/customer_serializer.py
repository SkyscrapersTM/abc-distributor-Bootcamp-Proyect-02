from apps.crm.customers.models import Customer

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    '''
        Class to convert a Customer object to a JSON format.
    '''
    # search method validate_<<name>>()
    # https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
    # valid that the entered field is in ruc format
    def validate_ruc(self, value):
        if len(value) != 11:
            raise serializers.ValidationError(
                "Debe ingresar un ruc válido.")
        return value

    # override method to_representation()
    # indicates fields to display converted into json without affecting the database
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'ruc': instance.ruc,
            'razón social': instance.name,
            'distrito': instance.district_id.name,
            'Categoría': instance.category_id.name
        }

    class Meta:

        model = Customer
        fields = '__all__'
