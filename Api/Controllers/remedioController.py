from DTO.remedioDto import RemedioDto
from models.Remedio import Remedio
from fastapi import APIRouter, Body
from repository.remedioRepository import criar_remedio, listar_remedios, consultar_remedios

router = APIRouter()

@router.get("/")
async def listarRemedios():
    remedios = listar_remedios() 
    return remedios

@router.post("/")
async def criarRemedios(data: RemedioDto = Body(...)):
    remedioOld = consultar_remedios(data.nome)
    if(remedioOld):
        return "Remédio "+data.nome+" já existe"

    remedio = Remedio(data.nome, data.quantidade, data.isComprimido)
    
    resultado = criar_remedio(remedio)
    return resultado