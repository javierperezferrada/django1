# -*- coding: utf-8 -*-
from io import BytesIO 
from reportlab.pdfgen import canvas 
from django.shortcuts import render 
from django.http import HttpResponse 
from biblioteca.models import Libro 

def formulario_buscar(request): 
     return render(request, 'formulario_buscar.html') 


def buscar(request): 
    errors = [] 
    if 'q' in request.GET: 
        q = request.GET['q'] 
        if not q: 
           errors.append('Por favor introduce un trmino de bsqueda.') 
        elif len(q) > 20: 
          errors.append('Por favor introduce un trmino de bsqueda menor a 20 caracteres.') 
        else: 
          libros = Libro.objects.filter(titulo__icontains=q) 
          return render(request, 'resultados.html',{'libros': libros, 'query': q}) 
 
    return render(request, 'formulario_buscar.html', {'errors': errors}) 

def convertir_pdf(request, pk): 
    # Obtenemos un queryset, para un determinado libro usando pk. 
    try: 
        libro = Libro.objects.get(id=pk) 
    except ValueError: # Si no existe llamamos a "pagina no encontrada". 
        raise Http404() 
    # Creamos un objeto HttpResponse con las cabeceras del PDF correctas. 
    response = HttpResponse(content_type='application/pdf') 
    # Nos aseguramos que el navegador lo abra directamente. 
    response['ContentDisposition'] = 'filename="archivo.pdf"' 
    buffer = BytesIO() 
    # Creamos el objeto PDF, usando el objeto BytesIO como si fuera un "archivo". 
    p = canvas.Canvas(buffer) 
    # Dibujamos cosas en el PDF. Aquí se genera el PDF. 
    # Consulta la documentación para una lista completa de funcionalidades. 
    p.roundRect(0, 750, 694, 120, 20, stroke=0, fill=1) 
    #p.setFont('Times­Bold',32) 
    p.setFillColorRGB(1,1,1) 
    p.drawString(100, 800, str(libro.titulo))#Obtenemos el titulo de un libro y la portada. 
    #p.drawImage(str(libro.portada.url), 100, 100, width=400, height=600) 
    # mostramos y guardamos el objeto PDF. 
    p.showPage() 
    p.save() 
    # Traemos el valor del bufer BytesIO y devolvemos la respuesta. 
    pdf = buffer.getvalue() 
    # Cerramos el bufer 
    buffer.close() 
    response.write(pdf) 
    return response 
