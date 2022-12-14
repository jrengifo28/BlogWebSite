from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Avatar


class UserEditionForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Editar email")
    password1 = forms.CharField(
        label="Ingrese la contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Verifique la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]


class AvatarForm(forms.ModelForm):
    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["imagen", "user"]
