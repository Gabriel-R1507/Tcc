from datetime import datetime, timedelta
from models.Vinculo import Vinculo
from models.Remedio import Remedio
from DTO.LinkRemedioDto import LinkRemedioDto
from DTO.ConsultarRemedioDto import ConsultarRemedioDto
from fastapi import APIRouter, Body
from repository.pacienteRepository import listar_vinculos

router = APIRouter()

@router.post("/medicamentos")
def listarRemedios(data: ConsultarRemedioDto):
    dia = datetime.strptime(data.dia, '%d/%m/%y')
    resultado = listar_vinculos(data.paciente, dia)

    return resultado

@router.post("/new")
async def criarPacientes(data: LinkRemedioDto = Body(...)):
    inicial = datetime.strptime(data.inicial, '%d/%m/%y %H:%M:%S')
    horario = inicial
    vezesAoDia = int(24 / data.frequencia)
    ranges = vezesAoDia * data.tempo

    #var remedio = get remedio by id (data.remedio)
    remedio = Remedio("testeRemedio", 10, True)
    d2 = remedio.quantidade - 2
    d1 = remedio.quantidade - 1
    for i in range(ranges):
        if(i % remedio.quantidade == 1 or i % remedio.quantidade == 2):
            vinc = Vinculo(data.paciente, data.remedio, horario, True)    
        
        else:
            vinc = Vinculo(data.paciente, data.remedio, horario, False)

        print(vinc.__dict__)
        #envia pro banco pra criar

        horario = horario + timedelta(hours=data.frequencia)

    return horario