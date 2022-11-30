# # from django.db import models
import datetime
import json

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
