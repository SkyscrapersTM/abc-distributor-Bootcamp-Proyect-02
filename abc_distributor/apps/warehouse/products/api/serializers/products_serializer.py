from rest_framework.serializers import ModelSerializer
from apps.warehouse.products.models import Product

class ProductSerializer(ModelSerializer):
    """
        Class to convert a Product object to a JSON format.
    """
    class Meta:
        model = Product
        #fields = ['code','name','percent_discount']
        fields = '__all__'


        