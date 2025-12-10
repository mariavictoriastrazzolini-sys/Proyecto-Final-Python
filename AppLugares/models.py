from django.db import models

# Create your models here.

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

class Experiencia(models.Model):
     comentario = models.TextField()
     puntuación = models.IntegerField()

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    precio_por_noche = models.CharField(max_length=50)
