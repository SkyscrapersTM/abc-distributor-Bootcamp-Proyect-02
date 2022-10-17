from apps.warehouse.products.models import ProductCategory

from rest_framework.serializers import ModelSerializer


class ProductCategorySerializer(ModelSerializer):
    """
        Clase para convertir un objeto ProductCategory a un formato JSON.
    """
    class Meta:
        model = ProductCategory
        fields = '__all__'
