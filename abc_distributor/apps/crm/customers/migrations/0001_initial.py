# Generated by Django 4.1.2 on 2022-10-16 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Código de Distrito')),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Moficación')),
            ],
            options={
                'verbose_name': 'Distrito',
                'db_table': 'district',
            },
        ),
    ]