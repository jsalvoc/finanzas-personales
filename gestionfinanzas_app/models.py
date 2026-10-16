from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, db_column="nombre_categoria")
    descripcion = models.CharField(max_length=150, null=True, db_column="descripcion_categoria")
    tipo = models.CharField(max_length=20, null=False, db_column="tipo_categoria")

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Cuenta(models.Model):
    nombre = models.CharField(max_length=50, null=False, db_column="nombre_cuenta")
    saldo_inicial = models.DecimalField(max_digits=12, decimal_places=0, null=False)

    def __str__(self):
        return self.nombre

class Presupuesto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column="id_categoria")
    monto_limite = models.DecimalField(max_digits=12, decimal_places=0, null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=False)

    def __str__(self):
        return f"Presupuesto: {self.monto_limite}"

class Transaccion(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, db_column="id_cuenta")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column="id_categoria")
    monto = models.DecimalField(max_digits=12, decimal_places=0, null=False, db_column="monto_transaccion")
    fecha = models.DateField(null=False, db_column="fecha_transaccion")
    descripcion = models.CharField(max_length=200, null=True, db_column="descripcion_transaccion")
    estado = models.CharField(max_length=20, default='COMPLETADA', db_column="estado_transaccion")

    def __str__(self):
        return f"{self.monto} - {self.estado}"