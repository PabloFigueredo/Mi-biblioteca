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
    promedio = df.groupby('autor__nombre')['calificacion__nivel'].mean().sort_values(ascending=False).head(10)
    plt.bar(promedio.index, promedio.values)
    plt.xlabel('Autor')
    plt.ylabel('Promedio de nivel de calificación')
    plt.title('Top 10: Promedio de nivel de calificación por autor')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_10_promedio_nivel_por_autor.png')
    plt.close()

def promedio_calificacion_por_nacionalidad():
    # Obtener los libros con la nacionalidad del autor y su nivel de calificación
    libros = Libro.objects.select_related('autor', 'calificacion').values(
        'autor__nacionalidad', 'calificacion__nivel'
    )
    df = pd.DataFrame(list(libros))

    if df.empty:
        print("No se encontraron datos.")
        return

    # Agrupar por nacionalidad y calcular el promedio de calificación
    promedio = df.groupby('autor__nacionalidad')['calificacion__nivel'].mean().sort_values(ascending=False)

    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(promedio.index, promedio.values)
    plt.xlabel('Nacionalidad')
    plt.ylabel('Promedio de calificación')
    plt.title('Promedio de calificación por nacionalidad de los autores')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('promedio_calificacion_por_nacionalidad.png')
    plt.close()

def libros_por_anio():
    libros = Libro.objects.values('fecha_lanzamiento', 'nombre')
    df = pd.DataFrame(list(libros))
    # Extraer el año de la fecha de lanzamiento
    df['anio'] = pd.to_datetime(df['fecha_lanzamiento'], errors='coerce').dt.year
    df['decada'] = (df['anio'] // 10) * 10  # Agrupar por década
    conteo_decadas = df['decada'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    plt.bar(conteo_decadas.index.astype(str), conteo_decadas.values)
    plt.xlabel('Década')
    plt.ylabel('Cantidad de libros')
    plt.title('Cantidad de libros publicados por década')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('libros_por_decada.png')
    plt.close()
if __name__ == "__main__":
    promedio_por_autor()

if __name__ == "__main__":
    promedio_calificacion_por_nacionalidad()

if __name__ == "__main__":
    promedio_por_genero()

if __name__ == "__main__":
    libros_por_anio()