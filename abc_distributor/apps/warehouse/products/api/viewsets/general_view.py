from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.products.api.serializers.general_serializer import ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides the standard actions
    """
    serializer_class = ProductCategorySerializer

    queryset = ProductCategorySerializer.Meta.model.objects.all()

    # indicates Json Web token(JWT)
    #permission_classes = (IsAuthenticated,)
