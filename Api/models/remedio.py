from django.db import models

class Remedio(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntField()
    IsComprimido = models.IntField()
