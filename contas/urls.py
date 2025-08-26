from django.urls import path
from . import views

urlpatterns = [
    path('criar_conta/', views.criar_conta, name='criar_conta'),
    path('exibir_conta/', views.exibir_conta, name='exibir_conta'),
    path('excluir_conta/', views.excluir_conta, name='excluir_conta'),
]