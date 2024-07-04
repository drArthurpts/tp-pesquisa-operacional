from django.shortcuts import render
from .models import Abrigo
from .forms import Desabrigado

def lista_abrigos(request):
    form = Desabrigado()
    abrigos = Abrigo.objects.all()
    return render(request, 'lista_abrigos.html', {'form': form, 'abrigos': abrigos})
