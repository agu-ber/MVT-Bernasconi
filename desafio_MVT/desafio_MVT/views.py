from django.http import HttpResponse
from django.template import loader

def home(request):

    plantilla = loader.get_template('home.html')
    documento = plantilla.render()

    return HttpResponse(documento)