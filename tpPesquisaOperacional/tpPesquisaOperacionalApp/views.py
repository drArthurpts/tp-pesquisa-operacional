from django.shortcuts import render, redirect
from .models import Abrigo
from .forms import DesabrigadoForm

def lista_abrigos(request):
    if request.method == "GET":
        form = DesabrigadoForm()
        abrigos = Abrigo.objects.all()
        return render(request, 'lista_abrigos.html', {'form': form, 'abrigos': abrigos})
    elif request.method == "POST":
        form = DesabrigadoForm(request.POST)
        if form.is_valid():
            desabrigado = form.save()
            return redirect('lista_abrigos')
        else:
            abrigos = Abrigo.objects.all()
            return render(request, 'lista_abrigos.html', {'form': form, 'abrigos': abrigos})
    else:
        return render(request, 'lista_abrigos.html', {'form': DesabrigadoForm(), 'abrigos': Abrigo.objects.all()})

