from django.urls import path

from blog.views import (
    # Vistas de la aplicación
    mostrar_inicio,
    MyLogin,
    MyLogout,


    # Vistas de Usuario
    UsuarioList,
    UsuarioDetalle,
    UsuarioCreacion,
    UsuarioActualizar,
    UsuarioBorrar,


    # Vistas de Pagina
    PaginaList,
    # PaginaDetalle,
)

urlpatterns = [
    # Path de la aplicación
    path("", mostrar_inicio, name='Inicio'),
    path("login/", MyLogin.as_view(), name='Login'),
    path("logout/", MyLogout.as_view(), name='Logout'),


    # Path de usuario
    path("usuario/list", UsuarioList.as_view(), name="UsuarioList"),
    path("r'(?P<pk>\d+)^$'", UsuarioDetalle.as_view(), name="UsuarioDetalle"),
    path("usuario-nuevo/", UsuarioCreacion.as_view(), name="UsuarioNuevo"),
    path("editar/<pk>", UsuarioActualizar.as_view(), name="UsuarioActualizar"),
    path("borrar/<pk>", UsuarioBorrar.as_view(), name="UsuarioBorrar"),


    # Path de Pagina
    path("pagina/list", PaginaList.as_view(), name="PaginaList"),
    # path("r'(?P<pk>\d+)^$'", PaginaDetalle.as_view(), name="PaginaDetalle"),
]
