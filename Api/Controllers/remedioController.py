from DTO.remedioDto import RemedioDto
from models.Remedio import Remedio
from fastapi import APIRouter, Body
from repository.remedioRepository import criar_remedio, listar_remedios

router = APIRouter()

@router.get("/")
async def listarRemedios():
    # remedios = await listar_remedios() 
    remedios = []
    rem1 = Remedio("remedio1", 2,True)
    remedios.append(rem1)
    remedios.append(Remedio("remedio2", 20, 1))
    remedios.append(Remedio("remedio3", 345, 0))
    remedios.append(Remedio("remedio4", 14, 1))
    remedios.append(Remedio("remedio5", 81, 1))

    remediosNome = []
    for remedio in remedios:
        remediosNome.append(remedio.nome)

    return remediosNome

@router.post("/")
async def criarRemedios(data: RemedioDto = Body(...)):
    print(data)
    remedio = Remedio(data.nome, data.quantidade, data.isComprimido)
    
    #consultar se ja existe remedio
    resultado = await criar_remedio(remedio)
    return resultado