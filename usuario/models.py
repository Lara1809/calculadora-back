from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='user_fotos/', null=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username