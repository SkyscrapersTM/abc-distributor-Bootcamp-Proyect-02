from rest_framework.serializers import ModelSerializer
from apps.warehouse.products.models import Product

class ProductSerializer(ModelSerializer):
    """
    Clase para convertir un objeto Product a un formato JSON.
    """
    class Meta:
        model = Product
        #fields = ['code','name','percent_discount']
        fields = '__all__'


        