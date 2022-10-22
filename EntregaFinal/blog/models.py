from django.db import models

# Models


class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    nombre_usuario = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=40)


class Pagina(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=256)
    autor = models.CharField(max_length=40)
    fecha = models.DateField()
    imagen = models.FileField()
