from django.db import models


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