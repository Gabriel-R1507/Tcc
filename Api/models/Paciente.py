# # from django.db import models
import json
from pydantic import BaseModel, Field


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


class Paciente(BaseModel):

    nome: str = Field(...)
    idade: int = Field(...)
    peso: int = Field(...)
    altura: int = Field(...)


    def __fields_set__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __dict__(self):
        return {
            "nome" : self.nome,
            "idade" : self.idade,
            "peso" : self.peso,
            "altura" : self.altura,
        }

    def getJson(self):
        dic = {
            "nome" : self.nome,
            "idade" : self.idade,
            "peso" : self.peso,
            "altura" : self.altura,
        }

        return json.dumps(dic)
