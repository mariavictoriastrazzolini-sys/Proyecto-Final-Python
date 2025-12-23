from django.http import HttpResponse
from django.shortcuts import render

from AppLugares.models import Alojamiento, Experiencia, Lugar
from AppLugares.forms import LugarForm, AlojamientoForm, ExperienciaForm

# VISTAS FBV

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


def buscar(request):
    nombre = request.GET.get("nombre", "")

    lugares = []

    if nombre:
        lugares = Lugar.objects.filter(nombre__icontains=nombre)

    return render(
        request,
        "AppLugares/resultadosBusqueda.html",
        {
            "lugares": lugares,
            "nombre": nombre
        }
    )
    

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# VISTAS CBV - LUGAR

class LugarListView(ListView):
    model = Lugar
    template_name = "AppLugares/lugar_list.html"

class LugarDetailView(DetailView):
    model = Lugar
    template_name = "AppLugares/lugar_detail.html"

class LugarCreateView(LoginRequiredMixin, CreateView):
    model = Lugar
    fields = ["nombre", "ciudad", "pais", "descripcion", "imagen"]
    template_name = "AppLugares/lugar_form.html"
    success_url = reverse_lazy("lugares")
    
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class LugarUpdateView(LoginRequiredMixin, UpdateView):
    model = Lugar
    fields = ["nombre", "ciudad", "pais", "descripcion", "imagen"]
    template_name = "AppLugares/lugar_form.html"
    success_url = reverse_lazy("lugares")

class LugarDeleteView(LoginRequiredMixin, DeleteView):
    model = Lugar
    template_name = "AppLugares/lugar_confirm_delete.html"
    success_url = reverse_lazy("lugares")

class AlojamientoListView(ListView):
    model = Alojamiento
    template_name = "alojamientos/alojamiento_list.html"

class ExperienciaListView(ListView):
    model = Experiencia
    template_name = "experiencias/experiencia_list.html"

def about(request):
    return render(request, "AppLugares/about.html")