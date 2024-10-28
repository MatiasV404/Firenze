from django.contrib import admin
from django.urls import path
from . import views  # Importación relativa para views.py en la misma carpeta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
