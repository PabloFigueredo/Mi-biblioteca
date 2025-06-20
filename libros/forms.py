from django import forms
from .models import Autor, Genero, Calificacion, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'nacionalidad']

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['nivel', 'descripcion']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre', 'autor', 'fecha_lanzamiento', 'genero', 'calificacion','portada','pdf']
        widgets = {
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date'}),
        }