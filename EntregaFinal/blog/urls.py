from django.contrib import admin
from django.urls import path

from blog.views import mostrar_inicio,  UsuarioList
""" listar_usuarios,"""

urlpatterns = [
    path("", mostrar_inicio, name='Inicio'),
    # path("lista-usuarios", listar_usuarios),
    path("usuario/list", UsuarioList.as_view(), name="UsuarioList"),
]
