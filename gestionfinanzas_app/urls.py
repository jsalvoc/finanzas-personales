from django.urls import path
from . import views

urlpatterns = [
    # Ruta principal o inicio de la aplicación
    path('', views.bienvenida, name='bienvenida'),
]