from apps.crm.customers.models import Customer

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    # busca método validate_<<name>>()
    # válida que el campo ingresado este en formato ruc
    def validate_ruc(self, value):
        if len(value) != 11:
            raise serializers.ValidationError(
                "Debe ingresar un ruc válido.")
        return value

    # sobreescribe método to_representation()
    # indica campos a mostrar en json sin afectar la base de datos
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
