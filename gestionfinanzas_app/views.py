from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    PerfilAcceso,
    TipoCuenta,
    Usuario,
    Categoria,
    Cuenta,
    Presupuesto,
    Transaccion,
    HistorialAuditoria,
    IndicadorGestion,
)
from .serializer import (
    PerfilAccesoSerializer,
    TipoCuentaSerializer,
    UsuarioSerializer,
    CategoriaSerializer,
    CuentaSerializer,
    PresupuestoSerializer,
    TransaccionSerializer,
    HistorialAuditoriaSerializer,
    IndicadorGestionSerializer,
)


# Vistas basadas en función (FBV) - Página de inicio y error 404
def index(request):
    nombre_plataforma = "FinanzasCentral"
    version_api = 2.0
    sistema_activo = True

    movimientos_recientes = [
        {"id_transaccion": "TX1001", "descripcion": "Pago de servicios básicos", "monto": 25000, "clasificacion": "gasto"},
        {"id_transaccion": "TX1002", "descripcion": "Compra de insumos operacionales", "monto": 150000, "clasificacion": "costo"},
        {"id_transaccion": "TX1003", "descripcion": "Mermas por daño de inventario", "monto": 12000, "clasificacion": "perdida"},
        {"id_transaccion": "TX1004", "descripcion": "Licencias de software", "monto": 45000, "clasificacion": "gasto"},
    ]

    total_operaciones = len(movimientos_recientes)

    contexto = {
        'plataforma': nombre_plataforma,
        'version': version_api,
        'estado': "Operativo" if sistema_activo else "En Mantenimiento",
        'movimientos': movimientos_recientes,
        'total_operaciones': total_operaciones,
    }

    return render(request, 'index.html', contexto)


def error_404(request, exception):
    contexto = {
        'mensaje_error': "El registro o ruta financiera que buscas no existe en nuestros sistemas."
    }
    return render(request, '404.html', contexto, status=404)


# Creación de vistas basadas en clase (CBV - ModelViewSet para CRUD REST completo)
class PerfilAccesoViewSet(viewsets.ModelViewSet):
    queryset = PerfilAcceso.objects.all()
    serializer_class = PerfilAccesoSerializer


class TipoCuentaViewSet(viewsets.ModelViewSet):
    queryset = TipoCuenta.objects.all()
    serializer_class = TipoCuentaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer


class PresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer


class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer


class HistorialAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = HistorialAuditoria.objects.all()
    serializer_class = HistorialAuditoriaSerializer


class IndicadorGestionViewSet(viewsets.ModelViewSet):
    queryset = IndicadorGestion.objects.all()
    serializer_class = IndicadorGestionSerializer
