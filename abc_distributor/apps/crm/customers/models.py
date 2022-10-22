from django.db import models


class District(models.Model):
    """
        District class.
        Ejem: Miraflores
    """

    id = models.AutoField(primary_key=True)

    # Atributo "code" => columna "code" de la tabla
    # Con el parámetro unique=True, le indicamos a Django que agregue un indice
    # tipo UNIQUE a la columna "code".
    # Código de distrito
    code = models.CharField(max_length=3, unique=True,
                            verbose_name="Código de Distrito")

    # indicates the name of the district
    name = models.CharField(max_length=40, verbose_name="Nombre")

    # indicates the date of registration of the district
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    # indicates the date of modification of the district
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        '''
            Special method that convert Python objects into strings
            by using __str__
        '''
        return f"{self.name}"

    class Meta:
        db_table = "district"
        verbose_name = "Distrito"


class CustomerCategory(models.Model):
    '''
        Customer Category Class
        For instance: Hotel
    '''

    id = models.AutoField(primary_key=True)

    # Atributo "code" => columna "code" de la tabla
    # Con el parámetro unique=True, le indicamos a Django que agregue un indice
    # tipo UNIQUE a la columna "code".
    # Código de categoría del cliente
    code = models.CharField(max_length=3, unique=True,
                            verbose_name="Código de Cliente")

    # indicates the name of the category
    name = models.CharField(max_length=40, verbose_name="Nombre")

    # indicates the date of registration of the category
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    # indicates the date of modification of the category
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        '''
            Special method that convert Python objects into strings
            by using __str__
        '''
        return f"{self.name}"

    class Meta:
        db_table = "customer_category"
        verbose_name = "Categoría de Cliente"


class Customer(models.Model):
    '''
        Client Class
    '''
    id = models.AutoField(primary_key=True)

    # single Registry of Taxpayers (RUC)
    ruc = models.CharField(max_length=11, unique=True, verbose_name="Ruc")

    # the business social reason
    name = models.CharField(max_length=60, blank=False,
                            default=None, verbose_name="Razon Social")

    # foreign_key: Distrito
    district_id = models.ForeignKey(District, on_delete=models.CASCADE,
                                    default=None, db_column="district_id", verbose_name="Distrito")

    # foreign_key: Categoria
    # indicate what industry the company is in
    category_id = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE,
                                    default=None, db_column="category_id", verbose_name="Categoría del Cliente")

    # company registration date
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    # date of the last modification of data in the company
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        '''
            Special method that convert Python objects into strings
            by using __str__
        '''
        return f"{self.name}"

    class Meta:
        db_table = "customer"
        verbose_name = "Cliente"
