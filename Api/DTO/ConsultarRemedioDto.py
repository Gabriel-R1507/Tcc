import json
from pydantic import BaseModel, Field

class ConsultarRemedioDto(BaseModel):
    paciente: str = Field(...)
    dia: str = Field(...)

    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
