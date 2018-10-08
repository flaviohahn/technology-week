from django.shortcuts import render
from .models import *



def technology_week(request):
    evento = Evento.objects.all()
    palestrante = PalestranteInstrutor.objects.all()
    palestra_oficina = PalestraOficina.objects.all()
    eventos = dict(listaEventos=evento, lista=palestrante,
                   listaPalestraOficina=palestra_oficina, )
    return render(request, 'blog/technology_week.html', eventos)



