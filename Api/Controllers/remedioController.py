from models.Remedio import Remedio
from fastapi import APIRouter, Body
from repository.remedioRepository import criar_remedio, listar_remedios

router = APIRouter()

@router.get("/")
async def listarRemedios():
    return await listar_remedios()

@router.post("/")
async def criarRemedios(remedio: Remedio = Body(...)):
    print(remedio)
    resultado = await criar_remedio(remedio)
    return resultado