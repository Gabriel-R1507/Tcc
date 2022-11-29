# # from django.db import models
import json
from pydantic import BaseModel, Field

class UsuarioCreateDto(BaseModel):

    login: str = Field(...)
    senha: str = Field(...)
    nome: str = Field(...)
    idade: str = Field(...)
    peso: str = Field(...)
    altura: str = Field(...)


    def __fields_set__(self, login, senha):
        self.login = login
        self.senha = senha

    def getJson(self):
        dic = {
            "login" : self.login,
            "senha" : self.senha,
        }

        return json.dumps(dic)
