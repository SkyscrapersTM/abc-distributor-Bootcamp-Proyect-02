from django.db import models
from decimal import Decimal

from apps.crm.customers.models import Customer
from apps.warehouse.products.models import Product


class DetailOrder(models.Model):
    '''
        Order Detail Class
    '''
    # contains the selected quantity of a single product
    quantity = models.PositiveSmallIntegerField()

    # foreign_key: Product
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, db_column="product", verbose_name="Producto", blank=True, null=True)

    # contains the total of the selected product
    total = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Total del Detalle", blank=True, null=True)

    # contains the total of the selected product without discount
    total_without_discount = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Total del Detalle sin Descuento", blank=True, null=True)

    # total purchase price
    total_purchase_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Sub Total", blank=True, null=True)

    def set_total_purchase_price(self):
        '''
            Calculate DetailOrder.quantity * product_id.purchase_price
            Set the total purchase price
        '''
        self.total_purchase_price = self.quantity * self.product_id.purchase_price

    def set_total(self):
        '''
            Calculate and set the total of the selected product.
        '''
        self.total = self.quantity * self.product_id.sale_price

    def set_total_without_discount(self):
        '''
            Calculate and set the total of the selected product without discount.
        '''
        self.total_without_discount = self.quantity * self.product_id.base_sale_price

    def save(self, *args, **kwargs):
        """
            Overriding the save method of the Model class.
        """

        self.set_total_purchase_price()
        self.set_total()
        self.set_total_without_discount()

        # calls the same save method already overwritten
        # https://www.geeksforgeeks.org/overriding-the-save-method-django-models/
        super(DetailOrder, self).save(*args, **kwargs)

    def __str__(self):
        '''
            Special method that convert Python objects into strings
            by using __str__
        '''
        return str(self.total)

    class Meta:

        db_table = "detail_order"
        verbose_name = "Detalle de Pedido"


class Order(models.Model):
    '''
        Order Class
        For instance:
            'Pedido' : {
                'code': '202200001',
                'customer_id': {
                    ...
                },
                'detail_id': [
                    {...},
                    {...},
                    {...}
                ],
                'sub_total': '500.00',
                'subtotal_without_discount': '620.00',
                'igv': '90.00',
                'total': '590.00',
                'discount_amount': '120',
            }
    '''
    id = models.AutoField(primary_key=True)

    # unique code for each order
    code = models.CharField(max_length=9, unique=True, verbose_name="Código")

    # foreign_key: Customer
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                    default=None, db_column="customer", verbose_name="Cliente", blank=True, null=True)

    # ManyToMany Relationship: Detail Order
    # contains order details
    detail_id = models.ManyToManyField(DetailOrder)

    # total purchase price
    total_purchase_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Sub Total", blank=True, null=True)

    # subtotal all order details
    sub_total = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Sub Total", blank=True, null=True)

    # subtotal all order details without discount
    sub_total_without_discount = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Total a pagar Sin Descuento", blank=True, null=True)

    # subtotal igv
    igv = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Igv", blank=True, null=True)

    # total sum of the order plus igv
    total = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Total a pagar", blank=True, null=True)

    # order discount if exist any
    discount_amount = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Monto Descuento")

    # register order date
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creación")

    # register modification date of the order
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificación")

    # register the date of the delivery order
    delivery_at = models.DateTimeField(
        verbose_name="Fecha de Entrega", blank=True, null=True)

    def set_total_purchase_price(self, total_purchase_price):
        '''
            Set the total purchase price
        '''
        self.total_purchase_price = total_purchase_price

    def set_sub_total(self, sub_total):
        '''
           Set the subtotal of the order. 
        '''
        self.sub_total = sub_total

    def set_sub_total_without_discount(self, sub_total_without_discount):
        '''
           Set the subtotal of the order without discount. 
        '''
        self.sub_total_without_discount = sub_total_without_discount

    def set_igv(self):
        '''
            Calculate and set the igv of the order.
        '''
        igv = (18/100.0)
        self.igv = self.sub_total * Decimal(igv)

    def set_total(self):
        '''
            Calculate and set the total of the order.
        '''
        self.total = self.sub_total + self.igv

    def set_discount_amount(self, sub_total_without_discount):
        '''
            Calculate and set the discount of the order.
        '''
        self.discount_amount = sub_total_without_discount - self.sub_total

    def __str__(self):
        '''
            Special method that convert Python objects into strings
            by using __str__
        '''
        return str(self.total)

    class Meta:

        db_table = "order"
        verbose_name = "Pedido"
