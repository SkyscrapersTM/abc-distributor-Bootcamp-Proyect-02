from django.db import models


class District(models.Model):
    """
        Clase Distrito.
        Ejem: Miraflores
    """

    id = models.AutoField(primary_key=True)

    # Atributo "code" => columna "code" de la tabla
    # Con el parámetro unique=True, le indicamos a Django que agregue un indice
    # tipo UNIQUE a la columna "code".
    # Código de distrito
    code = models.CharField(max_length=3, unique=True,
                            verbose_name="Código de Distrito")

    name = models.CharField(max_length=40, verbose_name="Nombre")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "district"
        verbose_name = "Distrito"


class CustomerCategory(models.Model):
    '''
        Clase Categoria de Cliente
        Ejemplo: Hotel
    '''

    id = models.AutoField(primary_key=True)

    # Atributo "code" => columna "code" de la tabla
    # Con el parámetro unique=True, le indicamos a Django que agregue un indice
    # tipo UNIQUE a la columna "code".
    # Código de categoría del cliente
    code = models.CharField(max_length=3, unique=True,
                            verbose_name="Código de Cliente")

    name = models.CharField(max_length=40, verbose_name="Nombre")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "customer_category"
        verbose_name = "Categoría de Cliente"


class Customer(models.Model):
    '''
        Clase Cliente
    '''
    id = models.AutoField(primary_key=True)

    ruc = models.CharField(max_length=11 ,unique=True, verbose_name="Ruc")

    name = models.CharField(max_length=60, blank=False,
                            default=None, verbose_name="Razon Social")

    # foreign_key: Distrito
    district_id = models.ForeignKey(District, on_delete=models.CASCADE,
                                    default=None, db_column="district_id", verbose_name="Distrito")

    # foreign_key: Categoria
    category_id = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE,
                                    default=None, db_column="category_id", verbose_name="Categoría del Cliente")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "customer"
        verbose_name = "Cliente"
