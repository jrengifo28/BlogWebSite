from re import L
from django.shortcuts import render
from blog.models import Usuario, Pagina

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Vistas de la aplicación


@login_required
def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def about_us(request):
    return render(request, "blog/about.html")


# def registrarse(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():


class MyLogin(LoginView):
    template_name = "blog/login.html"


class MyLogout(LogoutView):
    template_name = "blog/logout.html"


# Vistas de usuario

class UsuarioList(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "blog/listar-usuarios.html"


class UsuarioDetalle(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = "blog/usuario-detalle.html"


class UsuarioCreacion(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ["nombre", "apellido", "email", "nombre_usuario", "contraseña"]
    success_url = "/blog/usuario/list"


class UsuarioActualizar(LoginRequiredMixin, UpdateView):
    model = Usuario
    success_url = "/blog/usuario/list"
    fields = ["nombre", "apellido", "email", "nombre_usuario", "contraseña"]


class UsuarioBorrar(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = "/blog/usuario/list"


# Vistas de Paginas

class PaginaList(ListView):
    model = Pagina
    template_name = "blog/listar-paginas.html"


# class PaginaDetalle(DetailView):
#     model = Pagina
#     template_name = "blog/pagina-detalle.html"
