from django.urls import path
from . import views

urlpatterns = [
    path('salario/', views.salario, name='salario'),
    path('calculos/', views.calculos, name='casa'),
]
