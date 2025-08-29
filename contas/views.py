from django.shortcuts import render

# Create your views here.

def criar_conta(request):
    if request.method == 'POST':  # se o usuário enviou o formulário
        usuario = request.POST.get('username')
        plano = request.POST.get('plano')

        conta = User.objects.create_conta()
        conta.save()

def exibir_conta(request):
    pass

def excluir_conta(request):
    conta = request.conta

    if request.method == 'POST':
        conta.delete()          # apaga o usuário do banco
        return redirect('')  # volta para tela de login

