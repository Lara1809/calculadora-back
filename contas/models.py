from django.db import models
from django.contrib.auth.models import User 
from usuario.models import Usuario, Empresa, Servico, Categoria

# Create your models here.
class Conta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="contas")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="contas")
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True, blank=True, related_name="contas")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="contas")
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=50)
    data_vencimento = models.DateTimeField()
    data_pagamento = models.DateTimeField(null=True, blank=True)
    resultado = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.usuario.user.username}"