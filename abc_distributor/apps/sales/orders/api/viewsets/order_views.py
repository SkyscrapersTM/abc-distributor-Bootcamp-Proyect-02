from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from apps.sales.orders.models import Order
from apps.warehouse.products.models import Product
from apps.crm.customers.models import Customer
from apps.sales.orders.models import DetailOrder

from apps.sales.orders.api.serializers.order_serializer import OrderSerializer, OrderDetailSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides the standard actions
    """
    serializer_class = OrderSerializer
    queryset = OrderSerializer.Meta.model.objects.all()

    # indicates Json Web token(JWT)
    #permission_classes = (IsAuthenticated,)

    # Create a custom viewset
    @action(detail=False, methods=['get'], url_path='order-by-code')
    def order_by_id(self, request, pk=None):

        # get data from url parameter
        order_code = request.query_params.get('code')

        # returns the object with the parameter to search for
        order = Order.objects.get(code=order_code)

        # convert a Order object to a JSON format
        serializer = OrderSerializer(order)

        # display order data for the response
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a custom viewset
    @action(detail=False, methods=['get'], url_path='order-by-date')
    def order_by_date(self, request, pk=None):

        # get data from url parameter
        order_date = request.query_params.get('date')

        # returns objects with the filter to search
        order = Order.objects.filter(created_at=order_date)

        # check if an order instance exists
        if order:

            # convert a Order object to a JSON format
            serializer = OrderSerializer(order, many=True)

            # display orders data for the response
            return Response(serializer.data, status=status.HTTP_200_OK)

        # display status 400 for the response
        return Response({'mensaje': 'No se ha encontrado la orden.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a custom viewset
    @action(detail=False, methods=['get'], url_path='order-by-delivery-date')
    def order_by_delivery_date(self, request, pk=None):

        # get data from url parameter
        order_delivery_date = request.query_params.get('date')

        # returns objects with the filter to search
        order = Order.objects.filter(delivery_at=order_delivery_date)

        # check if an order instance exists
        if order:

            # convert a Order object to a JSON format
            serializer = OrderSerializer(order, many=True)

            # display orders data for the response
            return Response(serializer.data, status=status.HTTP_200_OK)

        # display status 400 for the response
        return Response({'mensaje': 'No se ha encontrado la orden.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a custom viewset
    @action(detail=False, methods=['get'], url_path='order-by-total')
    def order_by_total(self, request, pk=None):

        # get data from url parameter
        totalAmountHigherThan = request.query_params.get(
            'totalAmountHigherThan')

        # using Django QuerySet Filter https://www.w3schools.com/django/django_queryset_filter.php
        # returns objects with the filter to search
        order = Order.objects.filter(total__gte=totalAmountHigherThan)

        # check if an order instance exists
        if order:

            # convert a Order object to a JSON format
            serializer = OrderSerializer(order, many=True)

            # display orders data for the response
            return Response(serializer.data, status=status.HTTP_200_OK)

        # display status 400 for the response
        return Response({'mensaje': 'No se ha encontrado la orden.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a custom viewset
    @action(detail=False, methods=['get'], url_path='order-by-total-earnings')
    def order_by_total_earnings(self, request, pk=None):

        # get data from url parameter
        order_code = request.query_params.get('code')

        # returns the object with the parameter to search for
        order = Order.objects.get(code=order_code)

        # calculate earnings from obtained order data
        earnings = (order.sub_total - order.total_purchase_price)

        # display orders data for the response
        return Response({
            "numero_pedido": order.code,
            "venta_neta": order.sub_total,
            "costo_compra": order.total_purchase_price,
            "ganancia": earnings
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        '''
            Overwrite def create
        '''
        # get data from the petition (post)
        data = request.data

        # returns a Customer object with the data['parameter'] to search for
        new_customer = Customer.objects.get(
            ruc=data['customer_id']['ruc'])

        # create a Order object with data and new_customer
        new_order = Order.objects.create(
            code=data['code'], customer_id=new_customer, delivery_at=data['delivery_at'])

        # initialize variables

        total_purchase_price = 0
        sub_total_order = 0
        sub_total_without_discount = 0
        
        # iterate the details inside data
        for detail_order in data['detail_id']:

            # returns a Product object with the detail_order['product']['name'] to search for
            new_product = Product.objects.filter(
                name=detail_order['product_id']['name'],
                active=True)

            # create a Detail Order object with detail_order and new_product
            new_detail = DetailOrder.objects.create(
                quantity=detail_order['quantity'], product_id=new_product.first(
                )
            )

            # update the stock field of the product
            new_product.update(
                stock=new_product.first().stock - new_detail.quantity)

            # save the details in the database
            new_detail.save()

            # get the total purchase price from the order detail
            total_purchase_price = total_purchase_price + new_detail.total_purchase_price

            # get the subtotal of the order detail
            sub_total_order = sub_total_order + new_detail.total

            # get the subtotal of the order detail without discount
            sub_total_without_discount = sub_total_without_discount + \
                new_detail.total_without_discount
            
            # add each iterated detail to the order
            new_order.detail_id.add(new_detail)

        # sets the sum total of the purchase price of each detail
        new_order.set_total_purchase_price(total_purchase_price)

        # sets the sum total of the subtotal of each detail
        new_order.set_sub_total(sub_total_order)

        # sets the sum total of the subtotal of each detail without discount
        new_order.set_sub_total_without_discount(sub_total_without_discount)

        # set the igv of the order
        new_order.set_igv()

        new_order.set_total()

        # set the order total
        new_order.set_discount_amount(new_order.sub_total_without_discount)

        # update the order
        new_order.save()

        # convert a new_order object to a JSON format
        serializer = OrderSerializer(new_order)

        # display order data for the response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        '''
            Overwrite def retrieve
        '''
        # get the request instance
        instance = self.get_object()

        # convert instance to a JSON format
        # calls OrderDetailSerializer serializer to display the detail
        serializer = OrderDetailSerializer(instance=instance)

        # display order data for the response
        return Response(serializer.data, status=status.HTTP_200_OK)
