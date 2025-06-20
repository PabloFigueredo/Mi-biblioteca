from django.contrib import admin
from .models import Autor, Genero, Calificacion, Libro

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Calificacion)
admin.site.register(Libro)