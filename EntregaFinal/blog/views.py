from django.shortcuts import render
from blog.models import Usuario, Pagina

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.


def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


class UsuarioList(ListView):
    model = Usuario
    template_name = "blog/listar-usuarios.html"


class UsuarioDetalle(DetailView):
    model = Usuario
    template_name = "blog/usuario-detalle.html"


class PaginaList(ListView):
    model = Pagina
    template_name = "blog/listar-paginas.html"
