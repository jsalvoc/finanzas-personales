from django.urls import path, include
from rest_framework import routers
from gestionfinanzas_app import views

enrutador = routers.DefaultRouter()

enrutador.register(r'perfiles-acceso', views.PerfilAccesoViewSet)
enrutador.register(r'tipos-cuenta', views.TipoCuentaViewSet)
enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'categorias', views.CategoriaViewSet)
enrutador.register(r'cuentas', views.CuentaViewSet)
enrutador.register(r'presupuestos', views.PresupuestoViewSet)
enrutador.register(r'transacciones', views.TransaccionViewSet)
enrutador.register(r'historial-auditoria', views.HistorialAuditoriaViewSet)
enrutador.register(r'indicadores-gestion', views.IndicadorGestionViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]
