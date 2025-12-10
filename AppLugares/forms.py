from django import forms

class LugarForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre del lugar")
    ciudad = forms.CharField(max_length=100, label="Ciudad")
    pais = forms.CharField(max_length=100, label="País")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción")

class ExperienciaForm(forms.Form):
    comentario = forms.CharField(widget=forms.Textarea, label="Comentario")
    puntuación = forms.IntegerField(label="Puntuación")

class AlojamientoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre del alojamiento")
    tipo = forms.CharField(max_length=100, label="Tipo (hotel, hostel, cabaña…)") 
    precio_por_noche = forms.DecimalField(max_digits=8, decimal_places=2, label="Precio por noche")






