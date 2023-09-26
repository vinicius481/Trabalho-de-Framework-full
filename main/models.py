from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    USUARIOS = [
        (1, "aluno"),
        (2, "professor")
    ]

    cpf_cnpj = models.CharField(max_length=14, blank=False)
    phone = models.CharField(max_length=12)
    user = models.PositiveIntegerField(choices=USUARIOS, default=1)

    def __str__(self):
        return self.username
