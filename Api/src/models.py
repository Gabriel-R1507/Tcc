from django.db import models

# Create your models here.

class Paciente(models.Model):

    nome: str = models.CharField(max_length=128)
    idade: int = models.IntegerField
    peso: int = models.IntegerField
    altura: int = models.IntegerField
