from django.db import models

# Create your models here.


class Mensaje(models.Model):
    autor = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=256)
    fecha = models.DateField()
    archivo = models.FileField(blank=True)

    def __str__(self):
        return f"({self.fecha}) {self.autor}: {self.cuerpo}"
