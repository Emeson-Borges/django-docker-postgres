from typing import Any
from django.db import models
from uuid import uuid4

# Create your models here.
class Colaboradores(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100, name="nome")
    idade = models.IntegerField(name="idade")
    cidade = models.CharField(max_length=50, name="cidade")
    telefone = models.CharField(max_length=10, name="telefone")
    sexo = models.CharField(max_length=1, name="sexo")
    
    def __init__(self):
        return self.nome