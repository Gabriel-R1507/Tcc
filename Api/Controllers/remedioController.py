from models.Remedio import Remedio
from fastapi import APIRouter, Body
from repository.remedioRepository import criar_remedio, listar_remedios

router = APIRouter()

@router.get("/")
async def listarRemedios():
    # remedios = await listar_remedios() 
    remedios = []
    rem1 = Remedio()
    
    # rem1 = Remedio({"remedio1", 2,True})
    # rem1.isComprimido = True
    # rem1.nome = "remedio1"
    # rem1.quantidade = 2

    remedios.append(rem1)
    # remedios.append(Remedio("remedio2", 20, 1))
    # remedios.append(Remedio("remedio3", 345, 0))
    # remedios.append(Remedio("remedio4", 14, 1))
    # remedios.append(Remedio("remedio5", 81, 1))

    return remedios

@router.post("/")
async def criarRemedios(remedio: Remedio = Body(...)):
    print(remedio)
    resultado = await criar_remedio(remedio)
    return resultado