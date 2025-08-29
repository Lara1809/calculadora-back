from django.db import models
from django.contrib.auth.models import User 

class Plano(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    prazo = models.DateTimeField()
    data_assinatura = models.DateTimeField()

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True, related_name="usuarios")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    picture = models.ImageField(upload_to="usuarios/", null=True, blank=True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    servico = models.CharField(max_length=50)
    endereco = models.TextField()
    numero_celular = models.DecimalField(max_digits=9, decimal_places=0)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    slug = models.SlugField(unique=True)
    tipo_servico = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_servico


class Categoria(models.Model):
    slug = models.SlugField(unique=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
