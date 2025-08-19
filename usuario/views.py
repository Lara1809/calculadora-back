from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def listar(request):
    return render(request, 'listar.html')

def login(request):
    return render(request, 'login.html')

