from apps.warehouse.products.models import ProductCategory

from rest_framework.serializers import ModelSerializer


class ProductCategorySerializer(ModelSerializer):
    """
       Class to convert a Product Category object to a JSON format.
    """
    class Meta:
        model = ProductCategory
        fields = '__all__'
