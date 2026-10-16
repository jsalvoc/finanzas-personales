from rest_framework import serializers

from .models import PerfilAcceso, TipoCuenta, Usuario, Categoria, Cuenta
from .models import Presupuesto, Transaccion, HistorialAuditoria, IndicadorGestion


class PerfilAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilAcceso
        fields = ('__all__')


class TipoCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuenta
        fields = ('__all__')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('__all__')


class PresupuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presupuesto
        fields = ('__all__')


class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ('__all__')


class HistorialAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialAuditoria
        fields = ('__all__')


class IndicadorGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicadorGestion
        fields = ('__all__')
