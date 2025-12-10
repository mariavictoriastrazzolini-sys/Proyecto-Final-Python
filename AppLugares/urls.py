
from django.urls import path
from AppLugares import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('lugar/', views.lugar, name="Lugar"),  
    path('alojamiento/', views.alojamiento, name="Alojamiento"),
    path('experiencia/', views.experiencia, name="Experiencia"),
    path("crear_lugar/", views.crear_lugar, name="crear_lugar"),
    path("crear_alojamiento/", views.crear_alojamiento, name="crear_alojamiento"),
    path("crear_experiencia/", views.crear_experiencia, name="crear_experiencia"),
    path("busquedaLugar/", views.busquedaLugar, name="busquedaLugar"),
    path("buscar/", views.buscar)
]
