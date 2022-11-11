import json
from pydantic import BaseModel, Field

class Remedio():
    nome: str 
    quantidade: int
    isComprimido: bool

    def __init__(self, nome, quantidade, IsComprimido):
        self.nome = nome
        self.quantidade = quantidade
        self.IsComprimido = IsComprimido

    # def __fields_set__(self, nome, quantidade, IsComprimido):
    #     self.nome = nome
    #     self.quantidade = quantidade
    #     self.IsComprimido = IsComprimido
