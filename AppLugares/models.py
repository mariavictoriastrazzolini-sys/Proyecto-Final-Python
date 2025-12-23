from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    descripcion = RichTextField()   
    imagen = models.ImageField(upload_to="lugares/", blank=True, null=True)  
    fecha_creacion = models.DateField(auto_now_add=True) 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

class Experiencia(models.Model):
     comentario = models.TextField()
     puntuación = models.IntegerField()

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    precio_por_noche = models.CharField(max_length=50)
