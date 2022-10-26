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

# def listar_usuarios(request):
#     all_users = Usuario.objects.All()
#     contexto = {"usuarios_encontrados": all_users}
#     return render(request, "blog/listar-usuarios.html", contexto)


class PaginaList(ListView):
    model = Pagina
    template_name = "blog/pagina-list.html"
