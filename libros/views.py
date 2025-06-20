from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Genero, Calificacion, Libro, Resena
from .forms import AutorForm, GeneroForm, CalificacionForm, LibroForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Avg
from django.views.decorators.cache import never_cache
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import FileResponse, Http404
from django.views.decorators.http import require_GET
from django.db.models import Q
import os

# CRUD para Autor
@login_required
@never_cache
def listar_autores(request):
    autores_list = Autor.objects.all()
    paginator = Paginator(autores_list, 10)  # 10 autores por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'libros/listar_autores.html', {'page_obj': page_obj})

@login_required
@never_cache
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'libros/registrar_autor.html', {'form': form})

@login_required
@never_cache
def editar_autor(request, ):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'libros/editar_autor.html', {'form': form})

@login_required
@never_cache
def eliminar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'libros/eliminar_autor.html', {'objeto': autor})

# CRUD para Género (similar a Autor)
@login_required
@never_cache
def listar_generos(request):
    generos = Genero.objects.all()
    return render(request, 'libros/listar_generos.html', {'generos': generos})

@login_required
@never_cache
def crear_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_generos')
    else:
        form = GeneroForm()
    return render(request, 'libros/registrar_genero.html', {'form': form})

@login_required
@never_cache
def editar_genero(request, id):
    genero = get_object_or_404(Genero, id=id)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('listar_generos')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'libros/registrar_genero.html', {'form': form, 'genero': genero})

@login_required
@never_cache
def eliminar_genero(request, id):
    genero = get_object_or_404(Genero, id=id)
    if request.method == 'POST':
        genero.delete()
        return redirect('listar_generos')
    return render(request, 'libros/eliminar_genero.html', {'genero': genero})


# CRUD para Calificación
@login_required
@never_cache
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'libros/listar_calificaciones.html', {'calificaciones': calificaciones})

@login_required
@never_cache
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'libros/registrar_calificacion.html', {'form': form})

@login_required
@never_cache
def editar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('listar_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'libros/editar_calificacion.html', {'form': form, 'calificacion': calificacion})

@login_required
@never_cache
def eliminar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('listar_calificaciones')
    return render(request, 'libros/eliminar_calificacion.html', {'calificacion': calificacion})


# CRUD para Libro
@login_required
@never_cache
@login_required
@never_cache
def listar_libros(request):
    query = request.GET.get('q', '')
    libros = Libro.objects.all()
    if query:
        libros = libros.filter(
            Q(nombre__icontains=query) |
            Q(autor__nombre__icontains=query) |
            Q(genero__nombre__icontains=query)
        )
    paginator = Paginator(libros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'libros/listar_libros.html', {'page_obj': page_obj, 'query': query})

@login_required
@never_cache
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)  # Agrega request.FILES
        if form.is_valid():
            libro = form.save(commit=False)
            libro.usuario = request.user
            libro.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/registrar_libro.html', {'form': form})

@login_required
@never_cache
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if libro.usuario != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este libro.")

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form, 'libro': libro})

@login_required
@never_cache
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if libro.usuario != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este libro.")
   
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'libros/eliminar_libro.html', {'objeto': libro})

@login_required
@never_cache
def detalle_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    resenas = libro.resenas.all()
    ya_reseño = libro.resenas.filter(usuario=request.user).exists()
    puede_editar = libro.usuario == request.user

    # Calcula el promedio y la cantidad de reseñas
    promedio = resenas.aggregate(prom=Avg('calificacion'))['prom'] or 0
    cantidad = resenas.count()

    if request.method == 'POST' and not ya_reseño:
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario', '')
        if calificacion:
            Resena.objects.create(
                libro=libro,
                usuario=request.user,
                calificacion=calificacion,
                comentario=comentario
            )
            return redirect('detalle_libro', id=libro.id)

    return render(request, 'libros/detalle_libro.html', {
        'libro': libro,
        'resenas': resenas,
        'ya_reseño': ya_reseño,
        'puede_editar': puede_editar,
        'promedio': promedio,
        'cantidad': cantidad,
    })
@login_required
@xframe_options_exempt
def ver_pdf_archivo(request, id):
    from .models import Libro
    from django.conf import settings

    libro = Libro.objects.get(id=id)
    if not libro.pdf:
        raise Http404("PDF no encontrado")
    pdf_path = libro.pdf.path
    if not os.path.exists(pdf_path):
        raise Http404("PDF no encontrado")
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

@require_GET
@login_required
def descargar_pdf_libro(request, id):
    from .models import Libro
    libro = Libro.objects.get(id=id)
    if not libro.pdf:
        raise Http404("PDF no encontrado")
    pdf_path = libro.pdf.path
    if not os.path.exists(pdf_path):
        raise Http404("PDF no encontrado")
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_path)}"'
    return response

@login_required
def editar_resena(request, id):
    resena = get_object_or_404(Resena, id=id, usuario=request.user)
    if request.method == 'POST':
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario')
        if calificacion and comentario:
            resena.calificacion = calificacion
            resena.comentario = comentario
            resena.save()
            return redirect('detalle_libro', id=resena.libro.id)
    return render(request, 'libros/editar_resena.html', {'resena': resena})