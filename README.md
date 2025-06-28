# MI BIBLIOTECA
## Herramientas y versiones
- Python: 3.12
- Django: 5.2
- Django REST Framework: 3.16.0
- python-decouple
- sqlite3
- Pillow
## Instalacion
- Primero, tenés que asegurarte de tener Python instalado. Podés verificarlo con:
```bash
python3 --version
```
- Django requiere Python 3.10 o superior, así que si tenés una versión menor, vas a necesitar actualizarla.

- Después instalás pip y la herramienta para crear entornos virtuales:
```bash
sudo apt install python3-pip python3-venv
```
- Una vez hecho eso, creás una carpeta para tu proyecto:
```bash
mkdir mi_proyecto
cd mi_proyecto
```
- Dentro de esa carpeta, generás un entorno virtual con este comando:
```bash
python3 -m venv venv
```
- Y lo activás así:
```bash
source venv/bin/activate
```
- Cuando lo activás, vas a ver que en la terminal aparece algo como (venv) al principio de la línea, lo cual indica que estás dentro del entorno.
-Después actualizás pip para asegurarte de tener la última versión:
```bash
pip install --upgrade pip
```
- Con eso listo, instalás Django. Si querés la última versión disponible:
```bash
pip install django
```
- O, si preferís una versión específica (como la LTS 4.2), usás:
```bash
pip install django==4.2
```
- Una vez instalado, podés verificar que se haya instalado correctamente con:
```bash
django-admin --version
```
- Y ya podés crear el proyecto Django con:
```bash
django-admin startproject miweb
cd miweb
```
## Explicación del proyecto
Este proyecto es una plataforma de gestión de libros desarrollada con Django 5.2. Permite 
registrar, listar, editar y eliminar libros, autores, géneros y calificaciones. Incluye 
una interfaz web moderna y una API REST (usando Django REST Framework) para gestionar todos
los recursos desde aplicaciones externas o herramientas como Postman.
El sistema soporta autenticación de usuarios, subida de archivos (portadas y PDFs),
y está pensado para ser una base para bibliotecas, clubes de lectura o cualquier aplicación 
relacionada con la gestión de libros y sus metadatos.

## Registro de libros (codigo y resultado JSON)
### Codigo
- api_views.py
```bash
# Libro
class LibroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
```
- serializers.py
```bash
class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
```
### POSTMAN
```bash
POST http://127.0.0.1:8000/api/libros/
```
