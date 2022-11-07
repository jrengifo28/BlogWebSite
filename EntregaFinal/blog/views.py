from blog.models import Pagina, Avatar
from blog.forms import UserEditionForm, AvatarForm

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
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
    try:
        avatar = Avatar.objects.filter(user=request.user).first()
        contexto = {"avatar": avatar.imagen.url}
        return render(request, "blog/inicio.html", contexto)
    except:
        return render(request, "blog/inicio.html")


@login_required
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


@login_required
def editar_perfil(request):
    try:
        avatar = Avatar.objects.filter(user=request.user).first()
        user = request.user
        if request.method != "POST":
            form = UserEditionForm(initial={"email": user.email})
        else:
            form = UserEditionForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.email = data["email"]
                user.first_name = data["first_name"]
                user.last_name = data["last_name"]
                user.set_password(data["password1"])
                user.save()
                return render(request, "blog/inicio.html")

        contexto = {
            "user": user,
            "form": form,
            "avatar": avatar.imagen.url
        }
        return render(request, "blog/editar_Perfil.html", contexto)
    except:
        user = request.user
        if request.method != "POST":
            form = UserEditionForm(initial={"email": user.email})
        else:
            form = UserEditionForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.email = data["email"]
                user.first_name = data["first_name"]
                user.last_name = data["last_name"]
                user.set_password(data["password1"])
                user.save()
                return render(request, "blog/inicio.html")

        contexto = {
            "user": user,
            "form": form,
        }
        return render(request, "blog/editar_Perfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blog/inicio.html")

    contexto = {"form": form}
    return render(request, "blog/avatar_form.html", contexto)


class MyLogin(LoginView):
    template_name = "blog/login.html"


class MyLogout(LogoutView):
    template_name = "blog/logout.html"


# Vistas de Paginas

class PaginaList(LoginRequiredMixin, ListView):
    model = Pagina
    template_name = "blog/listar-paginas.html"


class PaginaDetalle(LoginRequiredMixin, DetailView):
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
