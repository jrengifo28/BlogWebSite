from django.urls import path

from blog.views import (
    # Vistas de la aplicación
    mostrar_inicio,
    about_us,
    registrarse,
    editar_perfil,
    agregar_avatar,
    MyLogin,
    MyLogout,

    # Vistas de Pagina
    PaginaList,
    PaginaDetalle,
    PaginaCreacion,
    PaginaActualizar,
    PaginaBorrar,
)

urlpatterns = [
    # Path de la aplicación
    path("", mostrar_inicio, name='Inicio'),
    path("login/", MyLogin.as_view(), name='Login'),
    path("logout/", MyLogout.as_view(), name='Logout'),
    path("aboutus", about_us, name='About_us'),
    path("registrarse/", registrarse, name='Registrarse'),
    path("editar-perfil/", editar_perfil, name='EditarPerfil'),
    path("agregar-avatar/", agregar_avatar, name='AgregarAvatar'),


    # Path de Pagina
    path("pagina/list", PaginaList.as_view(), name="PaginaList"),
    path("detalle/<pk>", PaginaDetalle.as_view(), name="PaginaDetalle"),
    path("pagina-nuevo/", PaginaCreacion.as_view(), name="PaginaNuevo"),
    path("editar/<pk>", PaginaActualizar.as_view(), name="PaginaActualizar"),
    path("borrar/<pk>", PaginaBorrar.as_view(), name="PaginaBorrar"),
]
