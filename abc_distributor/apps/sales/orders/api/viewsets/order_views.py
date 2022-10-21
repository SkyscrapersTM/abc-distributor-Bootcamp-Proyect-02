from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from apps.sales.orders.models import Order
from apps.warehouse.products.models import Product
from apps.crm.customers.models import Customer
from apps.sales.orders.models import DetailOrder

from apps.sales.orders.api.serializers.general_serializer import DetailOrderSerializer
from apps.sales.orders.api.serializers.order_serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    queryset = OrderSerializer.Meta.model.objects.all()

    @action(detail=False, methods=['get'], url_path='order-by-code')
    def order_by_id(self, request, pk=None):

        order_code = request.query_params.get('code')

        order = Order.objects.get(code=order_code)

        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='order-by-date')
    def order_by_date(self, request, pk=None):

        order_date = request.query_params.get('date')

        order = Order.objects.filter(created_at=order_date)

        if order:
            serializer = OrderSerializer(order, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'mensaje': 'No se ha encontrado la orden.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='order-by-delivery-date')
    def order_by_delivery_date(self, request, pk=None):

        order_delivery_date = request.query_params.get('date')

        order = Order.objects.filter(delivery_at=order_delivery_date)

        if order:
            serializer = OrderSerializer(order, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'mensaje': 'No se ha encontrado la orden.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='order-by-total')
    def order_by_total(self, request, pk=None):

        totalAmountHigherThan = request.query_params.get(
            'totalAmountHigherThan')

        # using Django QuerySet Filter https://www.w3schools.com/django/django_queryset_filter.php

        order = Order.objects.filter(total__gte=totalAmountHigherThan)

        if order:
            serializer = OrderSerializer(order, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'mensaje': 'No se ha encontrado la orden.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='order-by-total-earnings')
    def order_by_total_earnings(self, request, pk=None):

        order_code = request.query_params.get('code')

        order = Order.objects.get(code=order_code)

        earnings = (order.sub_total - order.total_purchase_price)

        serializer = OrderSerializer(order)

        return Response({
            "numero_pedido": order.code,
            "venta_neta": order.sub_total,
            "costo_compra": order.total_purchase_price,
            "ganancia": earnings
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        data = request.data

        new_customer = Customer.objects.get(
            ruc=data['customer_id']['ruc'])

        new_order = Order.objects.create(
            code=data['code'], customer_id=new_customer, delivery_at=data['delivery_at'])

        total_purchase_price = 0
        sub_total_order = 0
        sub_total_without_discount = 0

        for detail_order in data['detail_id']:

            new_product = Product.objects.filter(
                name=detail_order['product_id']['name'],
                active=True)

            new_detail = DetailOrder.objects.create(
                quantity=detail_order['quantity'], product_id=new_product.first()
            )

            new_product.update(
                stock=new_product.first().stock - new_detail.quantity)

            new_detail.save()

            total_purchase_price = total_purchase_price + new_detail.total_purchase_price

            sub_total_order = sub_total_order + new_detail.total

            sub_total_without_discount = sub_total_without_discount + \
                new_detail.total_without_discount

            new_order.detail_id.add(new_detail)

        new_order.set_total_purchase_price(total_purchase_price)

        new_order.set_sub_total(sub_total_order)

        new_order.set_sub_total_without_discount(sub_total_without_discount)

        new_order.set_igv()

        new_order.set_total()

        new_order.set_discount_amount(new_order.sub_total_without_discount)

        new_order.save()

        serializer = OrderSerializer(new_order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
