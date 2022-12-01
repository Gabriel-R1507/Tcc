from datetime import datetime, timedelta
from models.Vinculo import Vinculo
from models.Remedio import Remedio
from DTO.LinkRemedioDto import LinkRemedioDto
from DTO.ConsultarRemedioDto import ConsultarRemedioDto
from fastapi import APIRouter, Body
from repository.pacienteRepository import listar_vinculos, criar_vinculos
from repository.remedioRepository import consultar_remedios_id

router = APIRouter()

@router.post("/medicamentos")
def listarRemedios(data: ConsultarRemedioDto):
    resultado = listar_vinculos(data.paciente)

    return resultado

@router.post("/new")
async def criarVinculo(data: LinkRemedioDto = Body(...)):
    vinculos = []
    horario = datetime.strptime(data.inicial, '%d/%m/%y %H:%M:%S')
    vezesAoDia = int(24 / data.frequencia)
    ranges = (vezesAoDia * data.tempo)+1

    remedio = consultar_remedios_id(data.remedio)
    for i in range(1, ranges):
        if((i % remedio['quantidade'] == 0) or (i % remedio['quantidade'] == (remedio['quantidade'] -1))):
            vinc = Vinculo(data.paciente, data.remedio, horario, True)    
        else:
            vinc = Vinculo(data.paciente, data.remedio, horario, False)

        criar_vinculos(vinc)
        horario = horario + timedelta(hours=data.frequencia)
    
    return "vinculos criados corretamente!"