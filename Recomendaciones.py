import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usuarios.settings')
django.setup()

from libros.models import Libro
import pandas as pd

def recomendar_libros_por_genero():
    nombre_genero = input("Ingrese el nombre del género: ")

    # Obtener libros del género seleccionado con su nivel de calificación
    libros = Libro.objects.select_related('genero', 'calificacion').filter(
        genero__nombre=nombre_genero
    ).values('nombre', 'calificacion__nivel')

    df = pd.DataFrame(list(libros))

    if df.empty:
        print(f"No se encontraron libros para el género '{nombre_genero}'.")
        return

    # Ordenar por el nivel de calificación descendente
    df_ordenado = df.sort_values(by='calificacion__nivel', ascending=False)

    print(f"\nLibros recomendados para el género '{nombre_genero}':")
    for _, row in df_ordenado.iterrows():
        print(f"- {row['nombre']} (Nivel: {row['calificacion__nivel']})")

if __name__ == "__main__":
    recomendar_libros_por_genero()