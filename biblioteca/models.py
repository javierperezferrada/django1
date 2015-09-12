from django.db import models

class Editor(models.Model): 
    nombre = models.CharField(max_length=30) 
    domicilio = models.CharField(max_length=50) 
    ciudad = models.CharField(max_length=60) 
    estado = models.CharField(max_length=30) 
    pais = models.CharField(max_length=50) 
    website = models.URLField() 
 
class Autor(models.Model): 
    nombre = models.CharField(max_length=30) 
    apellidos = models.CharField(max_length=40) 
    email = models.EmailField() 

class Libro(models.Model): 
    titulo = models.CharField(max_length=100) 
    autores = models.ManyToManyField(Autor) 
    editor = models.ForeignKey(Editor) 
    fecha_publicacion = models.DateField() 
    portada = models.ImageField(upload_to='portadas') 
