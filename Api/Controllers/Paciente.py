# # from django.db import models
import json


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


class Paciente:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def printNome(self):
        print(self.nome)

    def getJson(self):
        dic = {
            "nome" : self.nome,
            "idade" : self.idade,
            "peso" : self.peso,
            "altura" : self.altura,
        }

        return json.dumps(dic)
