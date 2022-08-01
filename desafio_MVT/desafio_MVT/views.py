from tkinter.font import families
from django.http import HttpResponse
from django.template import loader
from AppDesafio.models import Familiar

def home(request):

    plantilla = loader.get_template('home.html')
    documento = plantilla.render()

    return HttpResponse(documento)

def familiares(request):

    entries = Familiar.objects.all()
    info = {"familiares": entries}

    plantilla = loader.get_template('familiares.html')
    documento = plantilla.render(info)

    return HttpResponse(documento)