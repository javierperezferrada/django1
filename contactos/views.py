from django.shortcuts import render
from contactos.forms import FormularioContactos
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect

def contactos(request):
    if request.method == 'POST':
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            mail = EmailMessage(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email', 'gypnetwork.info@gmail.com'),
                ['gypnetwork.info@gmail.com'],#direccion adonde llega
            )
            mail.send()
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormularioContactos()
    return render(request, 'formulario-contactos.html', {'form': form})