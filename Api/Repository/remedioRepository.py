from models.Remedio import Remedio
from bson import ObjectId
from utils.converterUtil import remedio_converter
from repository.database import get_database

db = get_database()

def criar_remedio(remedio: Remedio):
    created = db["remedio"].insert_one(remedio.__dict__)
    novo = db["remedio"].find_one({"_id": created.inserted_id })
    return remedio_converter(novo)

def consultar_remedios(nome: str):
    remedio = db["remedio"].find_one({"nome": nome })
    return remedio_converter(remedio)

def consultar_remedios_id(id: str):
    remedio = db["remedio"].find_one({"_id": ObjectId(id) })
    return remedio_converter(remedio)

def listar_remedios():
    remedios = []
    for post in db["remedio"].find():
        remedios.append(remedio_converter(post))

    return remedios