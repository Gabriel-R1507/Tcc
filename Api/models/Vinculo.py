# # from django.db import models
import datetime
import json
from pydantic import BaseModel, Field
from dataclasses import dataclass

# class Paciente():
#     # nome = models.CharField(max_length=100)
#     # idade = models.IntField()
#     # peso = models.CharField(max_length=100)
#     # altura = models.CharField(max_length=100)

#     def _init__(self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura


#     def printNome(self):
#         print(self.nome)


class Vinculo():

    paciente: str
    remedio: int
    data: datetime
    isLow: bool


    def __init__(self, paciente, remedio, data, isLow):
        self.paciente = paciente
        self.remedio = remedio
        self.data = data
        self.isLow = isLow

    def getJson(self):
        dic = {
            "nome" : self.nome,
            "idade" : self.idade,
            "peso" : self.peso,
            "altura" : self.altura,
        }

        return json.dumps(dic)
