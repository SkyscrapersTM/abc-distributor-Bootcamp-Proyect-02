from rest_framework import viewsets

from apps.warehouse.products.api.serializers.products_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer

    queryset = ProductSerializer.Meta.model.objects.all()

    
