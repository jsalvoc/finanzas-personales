"""
URL configuration for drf project.
"""
from django.contrib import admin
from django.urls import path, include
from gestionfinanzas_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    path('gestionfinanzas_app/', include('gestionfinanzas_app.urls')),
]

handler404 = 'gestionfinanzas_app.views.error_404'
