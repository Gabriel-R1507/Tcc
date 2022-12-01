import json
from pydantic import BaseModel, Field

class ConsultarRemedioDto(BaseModel):
    paciente: str = Field(...)

    def __fields_set__(self, paciente):
        self.paciente = paciente
