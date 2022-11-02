from django.db import models
from django.contrib.auth.models import User

# Models


class Pagina(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=256)
    autor = models.CharField(max_length=40)
    fecha = models.DateField()
    imagen = models.FileField()

    def __str__(self):
        return f"Titulo: {self.titulo} Subtitulo: {self.subtitulo} - ({self.autor})"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
