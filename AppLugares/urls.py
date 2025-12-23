
from django.urls import path
from AppLugares import views
from AppLugares.views import (LugarListView, LugarDetailView, LugarCreateView, LugarUpdateView, LugarDeleteView, AlojamientoListView, ExperienciaListView)


urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('lugar/', views.lugar, name="Lugar"),  
    path('alojamiento/', views.alojamiento, name="Alojamiento"),
    path('experiencia/', views.experiencia, name="Experiencia"),
    path("crear_lugar/", views.crear_lugar, name="crear_lugar"),
    path("crear_alojamiento/", views.crear_alojamiento, name="crear_alojamiento"),
    path("crear_experiencia/", views.crear_experiencia, name="crear_experiencia"),
    path("buscar/", views.buscar, name="buscar"),
    path("pages/", LugarListView.as_view(), name="lugares"),
    path("pages/<int:pk>/", LugarDetailView.as_view(), name="lugar_detail"),
    path("pages/create/", LugarCreateView.as_view(), name="lugar_create"),
    path("pages/<int:pk>/update/", LugarUpdateView.as_view(), name="lugar_update"),
    path("pages/<int:pk>/delete/", LugarDeleteView.as_view(), name="lugar_delete"),
    path("pages/alojamientos/", AlojamientoListView.as_view(), name="alojamientos"),
    path("pages/experiencias/", ExperienciaListView.as_view(), name="experiencias"),
    path("about/", views.about, name="about"),


]
