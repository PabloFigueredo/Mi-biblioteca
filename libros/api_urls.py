# libros/api_urls.py
from django.urls import path
from . import api_views

urlpatterns = [
    # Autor
    path('autores/', api_views.AutorListCreateAPIView.as_view(), name='api_autor_list_create'),
    path('autores/<int:pk>/', api_views.AutorRetrieveUpdateDestroyAPIView.as_view(), name='api_autor_detail'),
    # Genero
    path('generos/', api_views.GeneroListCreateAPIView.as_view(), name='api_genero_list_create'),
    path('generos/<int:pk>/', api_views.GeneroRetrieveUpdateDestroyAPIView.as_view(), name='api_genero_detail'),
    # Calificacion
    path('calificaciones/', api_views.CalificacionListCreateAPIView.as_view(), name='api_calificacion_list_create'),
    path('calificaciones/<int:pk>/', api_views.CalificacionRetrieveUpdateDestroyAPIView.as_view(), name='api_calificacion_detail'),
    # Libro
    path('libros/', api_views.LibroListCreateAPIView.as_view(), name='api_libro_list_create'),
    path('libros/<int:pk>/', api_views.LibroRetrieveUpdateDestroyAPIView.as_view(), name='api_libro_detail'),
]