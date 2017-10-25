from django.db import models


class Ticket(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField(max_length=1000)
    prioridad = models.IntegerField()
    servicio = models.CharField(max_length=100)
    archivo = models.FileField(blank=True, null=True)
