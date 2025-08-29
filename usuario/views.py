from django.shortcuts import render, redirect
from django.contrib import messages  #framework de mensagens
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout

def home_view(request):
    return render(request, 'home.html')

# usuario

def cadastrar(request):
    if request.method == 'POST':  # se o usuário enviou o formulário
        username = request.POST.get('username')
        picture = request.POST.get('picture')
        salario = request.POST.get('salario')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:          # se as duas senhas sao diferentes
            messages.error(request, "As senhas não conferem.")
        else:            # Cria o novo usuário no banco de dados
            user = User.objects.create_user(username=username, picture=picture, salario=salario, password=password1)
            usuario = Usuario.objects.create(user=user)
            user.save()

def login(request):
    if request.method == 'POST':  # se o usuário enviou o formulário
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)    # Verifica se existe um usuário com esse username e senha

        if user is not None:  
            login(request, user)  # cria a sessão do usuário
            return redirect('')  # redireciona para proxima página
        else:
            messages.error(request, "Usuário ou senha inválidos")   #mensagem de erro

    return render(request, '')

def exibir_usuario(request):
    usuario = {
        "username": user.username,
        "salario": user.salario,
        "picture": user.picture
    }
    return render(request, '', usuario)

def editar_usuario(request):
    user = request.user  # pega o usuário logado

    if request.method == 'POST':
        username = request.POST.get('username')
        picture = request.POST.get('picture')
        salario = request.POST.get('salario')

        user.username = username
        user.picture = picture
        user.salario = salario
        user.save()

        return redirect('')

def excluir_usuario(request):
    user = request.user

    if request.method == 'POST':
        user.delete()          # apaga o usuário do banco
        logout(request)        # encerra a sessão
        return redirect('')  # volta para tela de login

def logout(request):
    logout()
    return redirect('usuario_login')

# plano

def criar_plano(request):
    pass

def exibir_plano(request):
    pass

def excluir_plano(request):
    pass
