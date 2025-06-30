import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usuarios.settings')
django.setup()

from libros.models import Libro
import pandas as pd
import matplotlib.pyplot as plt

# Obtener los libros con su género y nivel de calificación
libros = Libro.objects.select_related('genero', 'calificacion').values(
    'genero__nombre', 'calificacion__nivel'
)

# Crear el DataFrame
df = pd.DataFrame(list(libros))

# Agrupar por género y calcular el promedio del nivel de calificación
promedio = df.groupby('genero__nombre')['calificacion__nivel'].mean().sort_values(ascending=False)

# Graficar
plt.bar(promedio.index, promedio.values)
plt.xlabel('Género')
plt.ylabel('Promedio de nivel de calificación')
plt.title('Promedio de nivel de calificación por género de libro')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('promedio_nivel_por_genero.png')
# plt.show()