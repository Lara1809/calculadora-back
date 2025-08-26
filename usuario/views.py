from django.shortcuts import render, redirect
from django.contrib import messages  #framework de mensagens
from django.contrib.auth import authenticate, login

def home_view(request):
    return render(request, 'home.html')

# usuario

def cadastrar(request):
    if request.method == 'POST':  # se o usuário enviou o formulário
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Verificações antes de criar o usuário
        if password1 != password2:          # se as duas senhas sao diferentes
            messages.error(request, "As senhas não conferem.")
        elif User.objects.filter(username=username).exists():   # se o usuario ja existe
            messages.error(request, "Esse usuário já existe.")
        elif User.objects.filter(email=email).exists():   # se ja existe um usuario com esse email
            messages.error(request, "Esse e-mail já está cadastrado.")
        else:
            # Cria o novo usuário no banco de dados
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Conta criada com sucesso!")   # mensagem se sucesso

def login(request):
    if request.method == 'POST':  # se o usuário enviou o formulário
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifica se existe um usuário com esse username e senha
        user = authenticate(request, username=username, password=password)
        if user is not None:  
            login(request, user)  # cria a sessão do usuário
            return redirect('')  # redireciona para proxima página
        else:
            messages.error(request, "Usuário ou senha inválidos")   #mensagem de erro

    return render(request, '')

def exibir_usuario(request):
    usuario = nome 
    email = email
    return render(request, '', {'usuario': usuario, 'email': email})

def editar_usuario(request):
    pass

def excluir_usuario(request):
    pass

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
