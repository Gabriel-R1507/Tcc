from datetime import datetime, timedelta
from models.Vinculo import Vinculo
from DTO.LinkRemedioDto import LinkRemedioDto
from fastapi import APIRouter, Body
from repository.pacienteRepository import listar_pacientes

router = APIRouter()

@router.post("/medicamentos")
def listarRemedios():
    resultado = listar_pacientes()
    return resultado

@router.post("/new")
async def criarPacientes(data: LinkRemedioDto = Body(...)):
    inicial = datetime.strptime(data.inicial, '%d/%m/%y %H:%M:%S')
    horario = inicial
    vezesAoDia = int(24 / data.frequencia)
    ranges = vezesAoDia * data.tempo

    for i in range(ranges):

        vinc = Vinculo(data.paciente, data.remedio, horario)
        print(vinc.__dict__)
        #envia pro banco pra criar

        horario = horario + timedelta(hours=data.frequencia)

    return horario