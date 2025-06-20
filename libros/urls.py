# libros/urls.py
from django.urls import path
from . import views

urlpatterns = [
       #path('', views.index, name='index'),  # Página principal con paginación
   # Autores
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:id>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:id>/', views.eliminar_autor, name='eliminar_autor'),

    #Generos
    path('generos/', views.listar_generos, name='listar_generos'),
    path('generos/crear/', views.crear_genero, name='crear_genero'),
    path('generos/editar/<int:id>/', views.editar_genero, name='editar_genero'),
    path('generos/eliminar/<int:id>/', views.eliminar_genero, name='eliminar_genero'),
    
    # Calificaciones
    path('calificaciones/', views.listar_calificaciones, name='listar_calificaciones'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('calificaciones/editar/<int:id>/', views.editar_calificacion, name='editar_calificacion'),
    path('calificaciones/eliminar/<int:id>/', views.eliminar_calificacion, name='eliminar_calificacion'),
    
    # Libros
    path('', views.listar_libros, name='listar_libros'),
    path('libros/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/<int:id>/pdf/', views.ver_pdf_archivo, name='ver_pdf_archivo'),
    path('libros/<int:id>/descargar_pdf/', views.descargar_pdf_libro, name='descargar_pdf_libro'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:id>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('resenas/<int:id>/editar/', views.editar_resena, name='editar_resena'),
]
