from array import array
from models.Remedio import Remedio
from utils.converterUtil import remedio_converter
from repository.database import get_database

db = get_database()

async def criar_remedio(remedio: Remedio):
    created = db["remedio"].insert_one(remedio.__dict__)
    novo = db["remedio"].find_one({"_id": created.inserted_id })
    return remedio_converter(novo)

async def consultar_remedios(nome: str):
    created = db["remedio"].find_one({"nome": nome })
    return created

async def listar_remedios():
    remedios = []
    for post in db["remedio"].find():
        remedios.append(remedio_converter(post))

    return remedios