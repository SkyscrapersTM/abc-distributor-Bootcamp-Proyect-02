from rest_framework import viewsets

from apps.warehouse.products.api.serializers.products_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides the standard actions
    """
    serializer_class = ProductSerializer

    queryset = ProductSerializer.Meta.model.objects.all()

    # indicates Json Web token(JWT)
    #permission_classes = (IsAuthenticated,)
