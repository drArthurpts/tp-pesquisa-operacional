from django.shortcuts import render, redirect
from .models import Abrigo, Desabrigado
from .forms import DesabrigadoForm
import pulp

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


def alocar_desabrigados(request):
    desabrigados = list(Desabrigado.objects.all())
    abrigos = list(Abrigo.objects.all())

    # Cria o problema de otimização
    prob = pulp.LpProblem("AlocacaoDesabrigados", pulp.LpMaximize)

    # Variáveis de decisão: x[i][j] = 1 se o desabrigado i for alocado ao abrigo j, 0 caso contrário
    x = pulp.LpVariable.dicts("x", ((i.id, j.id) for i in desabrigados for j in abrigos), cat='Binary')

    # Função objetivo: maximizar o número de desabrigados alocados
    prob += pulp.lpSum(x[i.id, j.id] for i in desabrigados for j in abrigos)

    # Restrição 1: Cada desabrigado pode ser alocado a no máximo um abrigo
    for i in desabrigados:
        prob += pulp.lpSum(x[i.id, j.id] for j in abrigos) <= 1

    # Restrição 2: Capacidade dos abrigos
    for j in abrigos:
        prob += pulp.lpSum(x[i.id, j.id] for i in desabrigados) <= j.capacidade

    # Resolve o problema
    prob.solve()

    # Verifica o status da solução
    alocacao = {}
    if pulp.LpStatus[prob.status] == 'Optimal':
        for i in desabrigados:
            for j in abrigos:
                if pulp.value(x[i.id, j.id]) == 1:
                    alocacao[i.nome] = j.nome

    return render(request, 'alocacao.html', {'alocacao': alocacao})