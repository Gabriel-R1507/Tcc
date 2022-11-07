# # from django.db import models
import json
from pydantic import BaseModel, Field


class Usuario(BaseModel):

    login: str = Field(...)
    senha: str = Field(...)
    idPaciente: int = Field(...)
    isAdmin: bool = Field(...)


    def __fields_set__(self, login, senha, IdPaciente, IsAdmin):
        self.login = login
        self.senha = senha
        self.IdPaciente = IdPaciente
        self.IsAdmin = IsAdmin

    def getJson(self):
        dic = {
            "login" : self.login,
            "senha" : self.senha,
            "IdPaciente" : self.IdPaciente,
            "IsAdmin" : self.IsAdmin,
        }

        return json.dumps(dic)
