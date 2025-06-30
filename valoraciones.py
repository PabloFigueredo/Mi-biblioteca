import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usuarios.settings')
django.setup()

from libros.models import Libro
import pandas as pd
import matplotlib.pyplot as plt

def promedio_por_genero():
    libros = Libro.objects.select_related('genero', 'calificacion').values(
        'genero__nombre', 'calificacion__nivel'
    )
    df = pd.DataFrame(list(libros))
    promedio = df.groupby('genero__nombre')['calificacion__nivel'].mean().sort_values(ascending=False)
    plt.bar(promedio.index, promedio.values)
    plt.xlabel('Género')
    plt.ylabel('Promedio de nivel de calificación')
    plt.title('Promedio de nivel de calificación por género de libro')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('promedio_nivel_por_genero.png')
    plt.close()  # <-- Esto cierra la figura
    # plt.show()

def promedio_por_autor():
    libros = Libro.objects.select_related('autor', 'calificacion').values(
        'autor__nombre', 'calificacion__nivel'
    )
    df = pd.DataFrame(list(libros))
    promedio = df.groupby('autor__nombre')['calificacion__nivel'].mean().sort_values(ascending=False)
    plt.bar(promedio.index, promedio.values)
    plt.xlabel('Autor')
    plt.ylabel('Promedio de nivel de calificación')
    plt.title('Promedio de nivel de calificación por autor')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('promedio_nivel_por_autor.png')
    plt.close()  # <-- Esto cierra la figura
    # plt.show()
def libros_por_anio():
    libros = Libro.objects.values('fecha_lanzamiento', 'nombre')
    df = pd.DataFrame(list(libros))
    # Extraer el año de la fecha de lanzamiento
    df['anio'] = pd.to_datetime(df['fecha_lanzamiento']).dt.year
    conteo = df['anio'].value_counts().sort_index()
    plt.bar(conteo.index.astype(str), conteo.values)
    plt.xlabel('Año de lanzamiento')
    plt.ylabel('Cantidad de libros')
    plt.title('Cantidad de libros publicados por año')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('libros_por_anio.png')
    plt.close()

if __name__ == "__main__":
    promedio_por_autor()

if __name__ == "__main__":
    promedio_por_genero()

if __name__ == "__main__":
    libros_por_anio()