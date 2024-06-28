from django.shortcuts import render
from .models import Abrigo
# Create your views here.
def lista_abrigos(request):
    abrigos = Abrigo.objects.all()
    return render(request, 'lista_abrigos.html', {'abrigos': abrigos})