from django.shortcuts import render

# Create your views here.
def lista_abrigos(request):
    return render(request, 'tpPesquisaOperacionalApp/lista_abrigos.html')