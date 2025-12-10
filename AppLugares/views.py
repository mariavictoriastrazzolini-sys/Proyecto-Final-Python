from django.http import HttpResponse
from django.shortcuts import render

from AppLugares.models import Alojamiento, Experiencia, Lugar
from AppLugares.forms import LugarForm, AlojamientoForm, ExperienciaForm


def inicio(request):
    return render (request , "AppLugares/inicio.html")

def lugar(request):
    lista_lugares = Lugar.objects.all()
    return render(request,"AppLugares/lugar.html",{"lugares": lista_lugares})

def alojamiento(request):
    lista_alojamientos = Alojamiento.objects.all()
    return render(request,"AppLugares/alojamiento.html",{"alojamientos":lista_alojamientos})

def experiencia(request):
    lista_experiencias = Experiencia.objects.all()
    return render(request,"AppLugares/experiencia.html",{"experiencias": lista_experiencias})


def crear_lugar(request):
    if request.method == "POST":
        miFormulario = LugarForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            lugar = Lugar(
                nombre=informacion["nombre"],
                ciudad=informacion["ciudad"],
                pais=informacion["pais"],
                descripcion=informacion["descripcion"],
            )
            lugar.save()
            return render(request, "AppLugares/inicio.html")
    else:
        miFormulario = LugarForm()

    return render(request, "AppLugares/LugarForm.html", {"miFormulario": miFormulario})

def crear_alojamiento(request):
    if request.method == "POST":
        miFormulario = AlojamientoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            alojamiento = Alojamiento(
                nombre=informacion["nombre"],
                tipo=informacion["tipo"],
                precio_por_noche=informacion["precio_por_noche"],
            )
            alojamiento.save()
            return render(request, "AppLugares/inicio.html")
    else:
        miFormulario = AlojamientoForm()

    return render(request, "AppLugares/AlojamientoForm.html", {"miFormulario": miFormulario})

def crear_experiencia(request):
    if request.method == "POST":
        miFormulario = ExperienciaForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            experiencia = Experiencia(
                comentario=informacion["comentario"],
                puntuación=informacion["puntuación"],
            )
            experiencia.save()
            return render(request, "AppLugares/inicio.html")
    
    else:
        miFormulario = ExperienciaForm()

    return render(request, "AppLugares/ExperienciaForm.html", {"miFormulario": miFormulario})


def busquedaLugar(request):
    return render (request, "AppLugares/BusquedaLugar.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre= request.GET ["nombre"]
        lugares= Lugar.objects.filter(nombre__icontains=nombre)
        return render (request, "AppLugares/resultadosBusqueda.html", {"lugares":lugares, "nombre":nombre})
    else:
        respuesta="No enviaste datos"
        return HttpResponse(respuesta)