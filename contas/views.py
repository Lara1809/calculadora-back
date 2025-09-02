from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Conta, Empresa, Servico, Categoria

# Create your views here.

def criar_conta(request):
    if request.method == 'POST':
        empresa_id = request.POST.get('empresa')
        servico_id = request.POST.get('servico')
        categoria_id = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        tipo = request.POST.get('tipo')
        data_vencimento = request.POST.get('data_vencimento')
        data_pagamento = request.POST.get('data_pagamento')
        resultado = request.POST.get('resultado')

        # Pega os objetos relacionados
        empresa = Empresa.objects.get(id=empresa_id)
        servico = Servico.objects.get(id=servico_id)
        categoria = Categoria.objects.get(id=categoria_id)

        # Cria a conta
        conta = Conta.objects.create(
            usuario=request.user,
            empresa=empresa,
            servico=servico,
            categoria=categoria,
            descricao=descricao,
            valor=valor,
            tipo=tipo,
            data_vencimento=data_vencimento,
            data_pagamento=data_pagamento,
            resultado=resultado
        )
        conta.save()

def exibir_conta(request):
    context = {
        'conta': conta
    }
    return render(request, '', context)

def excluir_conta(request):
    conta = request.conta

    if request.method == 'POST':
        conta.delete()          # apaga o usuário do banco
        return redirect('')  # volta para tela de login

