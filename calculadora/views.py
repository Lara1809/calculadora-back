from django.shortcuts import render
from django.contrib.auth.models import User
from contas.models import Conta, Servico, Categoria

# Create your views here.

def salario(request):
    if request.method == 'POST':
        salario = float(request.POST.get('salario', 0))
        extra = float(request.POST.get('extra', 0))
        salario_total = salario + extra

def calculos(request):
    total_contas = 0
    for Servico in Categoria:
        total_contas += Servico.valor
        
    saldo_restante = salario_total - total_contas
    
    contexto = {
        'total_contas': total_contas,
        'saldo_restante': saldo_restante,
    }
    
    return render(request, '', contexto)
