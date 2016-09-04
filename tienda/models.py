from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=140)
    precio = models.FloatField()
