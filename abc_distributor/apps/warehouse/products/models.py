from django.db import models

from apps.sales.currency.models import Currency

from django.core.validators import MinValueValidator, MaxValueValidator


class UnitMeasureCategory(models.Model):
    """
        Clase de Categoría de Unidades de Medida.
        Ejemplo: Peso, Volumen, Longitud
    """

    # Atributo "id" => columna "id" de la tabla
    # Identificador de registro de nuestra tabla.
    id = models.AutoField(primary_key=True, db_column="id")

    # Atributo "code" => columna "code" de la tabla
    # Con el parámetro unique=True, le indicamos a Django que agregue un indice
    # tipo UNIQUE a la columna "code".
    # Código de Categoría de Unidad de Medida
    code = models.CharField(max_length=3, unique=True, verbose_name="Código")

    # Atributo "name" => columna "name" de la tabla
    # Nombre de Categoría de Unidad de Medida
    name = models.CharField(max_length=30, verbose_name="Nombre")

    # Atributo "created_at" => columna "created_at" de la tabla
    # Fecha de creación de un registro
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    # Atributo "updated_at" => columna "updated_at" de la tabla.
    # Fecha de última modificación de un registro
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self) -> str:
        """
        Método para devolver un string que represente al objeto
        """
        return self.name

    class Meta:
        """
        Clase Meta:
        Clase de Django para agregar opciones adicionales a nuestro modelo.
        Link: https://docs.djangoproject.com/en/4.1/ref/models/options/
        """

        # Nombre que recibirá nuestro modelo en la base de datos.
        db_table = "unit_measure_category"

        # Texto que aparecerá en nuestra aplicación.
        verbose_name = "Categoría de Unidades de Medida"


class UnitMeasure(models.Model):
    """
    Clase Unidad de Medida.

    Ejem: 
        Kg -> Categoría (Peso)
        Litro -> Categoría (Volumen), 
        g (gramo) -> Categoría (Peso) 
    """

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=3, unique=True, verbose_name="Código")
    name = models.CharField(max_length=30, verbose_name="Nombre")

    # Atributo tipo Foreign Key (FK).
    # FK: categoría de unidad de medida
    # Le indicamos a Django que el atributo "unit_measure_category_id" se convierta en una FK
    # en nuestra base de datos.
    unit_measure_category_id = models.ForeignKey(UnitMeasureCategory, on_delete=models.CASCADE,
                                                 default=None, db_column="unit_measure_category_id", verbose_name="Categoría de Unidad de Medida")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "unit_measure"

        verbose_name = "Unidades de Medida"


class ProductCategory(models.Model):
    """
    Clase Categoría de Producto.
    Ejem: Abarrotes
    """

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=3, unique=True, verbose_name="Código")
    name = models.CharField(max_length=50, verbose_name="Nombre")
    percent_discount = models.PositiveSmallIntegerField(default=0, validators=[
                                                        MinValueValidator(0), MaxValueValidator(50)], verbose_name="Descuento (%)")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        #self.percent_discount = 5
        super(ProductCategory, self).save(*args, **kwargs)

    class Meta:
        db_table = "product_category"
        verbose_name = "Categoría de Producto"


class Product(models.Model):

    id = models.AutoField(primary_key=True)

    # Atributo "code" => columna "code" de la tabla
    # Con el parámetro unique=True, le indicamos a Django que agregue un indice
    # tipo UNIQUE a la columna "code".
    # Código de distrito
    code = models.CharField(max_length=6, unique=True, verbose_name="Código")

    # indicate the name of the product
    name = models.CharField(max_length=60, blank=False,
                            default=None, verbose_name="Nombre")

    # imagen del producto
    # image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)

    # foreign_key: categoría de producto
    # indicate in which category the product is located
    product_category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
                                            default=None, db_column="product_category_id", verbose_name="Categoría Producto")

    # foreign_key: unidad de medida
    # indicates the unit of measure of the product
    unit_measure_id = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE,
                                        default=None, db_column="unit_measure_id", verbose_name="Unidad de Medida")

    # foreign_key: Moneda
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, default=None, db_column="currency_id", verbose_name="Moneda")

    # indicates the purchase price of the product.
    purchase_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Precio de Compra")

    # indicates the base selling price of the product
    base_sale_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Precio de Venta Base")

    # indicates the product discount (%)
    # require: from django.core.validators
    percent_discount = models.PositiveSmallIntegerField(default=0, validators=[
                                                        MinValueValidator(0), MaxValueValidator(60)], verbose_name="Descuento (%)")

    # indicates the discount amount of the product
    discount_amount = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Monto Descuento", blank=True, null=True)

    # indicates the selling price of the product
    sale_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Precio de Venta", blank=True, null=True)

    # indicates the quantity of the product available
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")

    # activo: BooleanField
    active = models.BooleanField(default=True, verbose_name="Activo")

    # product registration date
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creación")

    # product modification date
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificación")

    def __str__(self):
        '''
            Special method that convert Python objects into strings
            by using __str__
        '''
        return self.name

    def calc_discount_amount(self):
        '''
            Compare category discount and product discount,
            then apply the base sale price with the highest discount
        '''

        if self.product_category_id.percent_discount > self.percent_discount:
            self.discount_amount = round(
                (int(self.product_category_id.percent_discount)/100)*float(self.base_sale_price), 2)

        else:
            self.discount_amount = round(
                (int(self.percent_discount)/100)*float(self.base_sale_price), 2)

    def save(self, *args, **kwargs):
        """
            Overriding the save method of the Model class.
        """
        # calculate discount amount
        self.calc_discount_amount()

        # calculate the sale price
        self.sale_price = float(self.base_sale_price) - \
            float(abs(self.discount_amount))

        # calls the same save method already overwritten
        # https://www.geeksforgeeks.org/overriding-the-save-method-django-models/
        super(Product, self).save(*args, **kwargs)

    class Meta:
        db_table = "product"
        verbose_name = "Producto"
