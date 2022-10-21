from rest_framework.serializers import ModelSerializer

from apps.sales.orders.models import Order

class OrderSerializer(ModelSerializer):

    class Meta:

        model = Order
        fields = '__all__'

    def to_representation(self, instance):

        return {
            'id_pedido': instance.id,
            'numero_de_pedido': instance.code,
            'fecha_de_pedido': instance.created_at,
            'razon_social_del_cliente': instance.customer_id.name,
            'fecha_de_entrega': instance.delivery_at,
            'importe_subtotal': f"S/ {instance.sub_total}",
            'igv': f"S/ {instance.igv}",
            'importe_total': f"S/ {instance.total}",
            "importe_total_de_descuento": f"S/{instance.discount_amount}"
        }


class OrderDetailSerializer(ModelSerializer):

    class Meta:

        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        data_detail = []

        for detail in instance.detail_id.all():
            data_detail.append({
                "id": detail.id,
                "producto": detail.product_id.name,
                "precio_base": f"S/ {detail.product_id.base_sale_price}",
                "precio_venta": f"S/ {detail.product_id.sale_price}",
                "cantidad": detail.quantity,
                "total": f"S/ {detail.total}"
                
            })

        data_customer = {
            "razon_Social": instance.customer_id.name,
            "ruc": instance.customer_id.ruc,
            "categoria": instance.customer_id.category_id.name,
            "distrito": instance.customer_id.district_id.name
        }

        return {
            'id_pedido': instance.id,
            'numero_de_pedido': instance.code,
            'fecha_de_pedido': instance.created_at,
            'cliente': data_customer,
            'fecha_de_entrega': instance.delivery_at,
            'detalle': data_detail,
            'importe_subtotal': f"S/ {instance.sub_total}",
            'igv': f"S/ {instance.igv}",
            'importe_total': f"S/ {instance.total}",
            "importe_total_de_descuento": f"S/{instance.discount_amount}"
        }
