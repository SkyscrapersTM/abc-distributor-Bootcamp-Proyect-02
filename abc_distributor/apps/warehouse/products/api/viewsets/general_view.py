from rest_framework import viewsets

from apps.warehouse.products.api.serializers.general_serializer import ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = ProductCategorySerializer
    queryset = ProductCategorySerializer.Meta.model.objects.all()
