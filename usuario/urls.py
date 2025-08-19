from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar, name='listar'),
    path('login/', views.login, name='login'),
]