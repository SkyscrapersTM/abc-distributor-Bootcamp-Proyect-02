# Generated by Django 4.1.2 on 2022-10-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Stock'),
        ),
    ]
