from django.shortcuts import render
from blog.models import Pagina

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


def registrarse(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()
            return render(
                request,
                "blog/inicio.html",
                {"mensaje": f"Bienvenido: {username_capturado}"},
            )
    else:
        form = UserCreationForm()
    return render(request, "blog/registro.html", {"form": form})


class MyLogin(LoginView):
    template_name = "blog/login.html"


class MyLogout(LogoutView):
    template_name = "blog/logout.html"


# Vistas de Paginas

class PaginaList(ListView):
    model = Pagina
    template_name = "blog/listar-paginas.html"


class PaginaDetalle(DetailView):
    model = Pagina
    template_name = "blog/pagina-detalle.html"


class PaginaCreacion(LoginRequiredMixin, CreateView):
    model = Pagina
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha", "imagen"]
    success_url = "/blog/pagina/list"


class PaginaActualizar(LoginRequiredMixin, UpdateView):
    model = Pagina
    success_url = "/blog/pagina/list"
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha", "imagen"]


class PaginaBorrar(LoginRequiredMixin, DeleteView):
    model = Pagina
    success_url = "/blog/pagina/list"
