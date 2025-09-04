from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import LoginForm, CadastrarForm
from .models import Role, Usuario, Plano

def home_view(request):
    return render(request, 'home.html')

# usuario

def cadastrar(request):
    if request.method == 'POST':
        form = CadastrarForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = User.objects.create_user(username=username, password=password)

            usuario = Usuario.objects.create(user=user, role=role)

            return redirect('') 
    else:
        form = CadastrarForm()

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('')
    else:
        form = LoginForm()

    return render(request, '', {'form': form})

def exibir_usuario(request):
    usuario = {
        "user": Usuario.user,
        "plano": Usuario.plano,
        "picture": Usuario.picture,
    }
    return render(request, '', usuario)

def editar_usuario(request):
    pass

def excluir_usuario(request):
    user = request.user

    if request.method == 'POST':
        user.delete()          # apaga o usuário do banco
        logout(request)        # encerra a sessão
        return redirect('')  # volta para tela de login

def logout(request):
    logout(request)
    return redirect('home')

# plano

def criar_plano(request):
    pass

def exibir_plano(request):
    pass

def excluir_plano(request):
    pass
