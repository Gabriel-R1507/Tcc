import json
from pydantic import BaseModel, Field

class RemedioDto(BaseModel):
    nome: str = Field(...)
    quantidade: int = Field(...)
    isComprimido: bool = Field(...)

    def __init__(self, nome, quantidade, isComprimido):
        self.nome = nome
        self.quantidade = quantidade
        self.isComprimido = isComprimido
