# # from django.db import models
import json

class Usuario():

    login: str
    senha: str
    idPaciente: int
    isAdmin: bool


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
