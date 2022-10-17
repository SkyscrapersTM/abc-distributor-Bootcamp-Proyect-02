from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.products.api.serializers.general_serializer import ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = ProductCategorySerializer

    permission_classes = (IsAuthenticated,)

    queryset = ProductCategorySerializer.Meta.model.objects.all()
