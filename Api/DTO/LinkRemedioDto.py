# # from django.db import models
import datetime
import json
from pydantic import BaseModel, Field

class LinkRemedioDto(BaseModel):

    paciente: str = Field(...)
    remedio: str = Field(...)
    tempo: int = Field(...)
    frequencia: int = Field(...)
    inicial: str = Field(...)


    def __fields_set__(self, paciente, remedio, tempo, frequencia, inicial):
        self.paciente = paciente
        self.remedio = remedio
        self.tempo = tempo
        self.frequencia = frequencia
        self.inicial = inicial

    def getJson(self):
        dic = {
            "login" : self.login,
            "senha" : self.senha,
        }

        return json.dumps(dic)
