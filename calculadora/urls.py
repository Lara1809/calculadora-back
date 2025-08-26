from django.urls import path
from . import views

urlpatterns = [
    path('salario/', views.salario, name='salario'),
    path('casa/', views.calculo_casa, name='casa'),
    path('alimentacao/', views.calculo_alimentacao, name='alimentacao'),
    path('saude_beleza/', views.calculo_saude_beleza, name='saude_beleza'),
    path('transposte/', views.calculo_transposte, name='transposte'),
    path('educacao/', views.calculo_educacao, name='educacao'),
    path('extra/', views.calculo_extra, name='extra'),
    path('gastos_totais/', views.gastos_totais, name='gastos_totais'),
]
