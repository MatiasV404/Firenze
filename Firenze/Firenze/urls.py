from django.contrib import admin
from django.urls import path
from . import views  # Importación relativa para views.py en la misma carpeta
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('barbers/', views.barbers, name='barbers'),
    path('registro/', views.registro, name='registro'),
    path('services/', views.services, name='services'),
    path('login/', views.login, name='login'),
    path('salir/', views.cerrar_sesion, name='cerrar_sesion'),
    path('carrito/', views.carrito, name='carrito'),
]
