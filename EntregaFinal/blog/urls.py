from django.contrib import admin
from django.urls import path

from blog.views import mostrar_inicio

urlpatterns = [
    path("", mostrar_inicio, name='Inicio'),
]
