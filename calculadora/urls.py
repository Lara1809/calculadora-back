from django.urls import path
from . import views

urlpatterns = [
    path('salario/', views.salario, name='salario'),
    path('casa/', views.casa, name='casa'),
    path('alimentacao/', views.alimentacao, name='alimentacao'),
]
