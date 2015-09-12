from django.conf.urls import include, url
from django.contrib import admin
from django1.views import hola , fecha_actual, horas_adelante
from biblioteca import views 


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hola/', hola),
    url(r'^fecha/', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante), 
    url(r'^fbuscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),


]
