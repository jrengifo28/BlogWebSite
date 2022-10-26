from django.contrib import admin
from django.urls import path

from blog.views import (
    mostrar_inicio,
    UsuarioList,
    PaginaList,
    UsuarioDetalle,
)

urlpatterns = [
    path("", mostrar_inicio, name='Inicio'),
    path("usuario/list", UsuarioList.as_view(), name="UsuarioList"),
    path("pagina/list", PaginaList.as_view(), name="PaginaList"),
    path("r'(?P<pk>\d+)^$'", UsuarioDetalle.as_view(), name="UsuarioDetalle"),
]
