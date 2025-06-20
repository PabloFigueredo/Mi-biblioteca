# nombre_de_la_app/models.py
from django.db import models
from django.conf import settings
import os
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del género

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    nivel = models.IntegerField(unique=True)  # Nivel de calificación (1, 2, 3, etc.)
    descripcion = models.TextField(max_length=500, default="Sin descripción")  # Valor por defecto

    def __str__(self):
        return f"{self.nivel} - {self.descripcion}"

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)  # Nuevo campo para archivo
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)  # Cambia pdf_url por pdf
    genero = models.ForeignKey(Genero, null=True, blank=True, on_delete=models.SET_NULL)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Nuevo campo
   
    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        # Elimina la portada si existe
        if self.portada and os.path.isfile(self.portada.path):
            os.remove(self.portada.path)
        # Elimina el PDF si existe
        if self.pdf and os.path.isfile(self.pdf.path):
            os.remove(self.pdf.path)
        super().delete(*args, **kwargs)
   
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField(max_length=1000, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('libro', 'usuario')

    def __str__(self):
        return f"{self.usuario} - {self.libro} ({self.calificacion})"