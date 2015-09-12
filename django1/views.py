from django.http import Http404, HttpResponse 
from django.shortcuts import render 


import datetime 

def hola(request): 
    return HttpResponse("Hola Mundo") 

def fecha_actual(request): 
    ahora = datetime.datetime.now() 
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora}) 



def horas_adelante(request, offset): 
    try: 
        offset = int(offset) 
    except ValueError: 
        raise Http404()  
    dt= datetime.datetime.now()+datetime.timedelta(hours=offset)        
    html = "<html><body><h1>En %s hora(s), seran:</h1> <h3> %s</h3></body></html>" % (offset, dt) 
    return HttpResponse(html)  

