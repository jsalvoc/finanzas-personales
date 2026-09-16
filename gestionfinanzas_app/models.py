from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=150, null=True)
    tipo = models.CharField(max_length=20, null=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    saldo_inicial = models.DecimalField(max_digits=12, decimal_places=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    monto = models.DecimalField(max_digits=12, decimal_places=0, null=False)
    fecha = models.DateField(null=False)
    descripcion = models.CharField(max_length=200, null=True)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.monto} - {self.categoria.nombre}"