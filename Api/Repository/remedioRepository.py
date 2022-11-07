from array import array
from models.Remedio import Remedio
from utils.converterUtil import remedio_converter
from repository.database import get_database

db = get_database()
async def criar_remedio(remedio: Remedio):
    print(remedio.__dict__)
    created = await db["remedio"].insert_one(remedio.__dict__)
    # novo = await remedio_collection.find_one({"_id": created.inserted_id })
    return "deu certo"

async def listar_remedios():
    remedios = []
    remedios.append(await remedio_collection.find_one({}))
    # cursor = remedio_collection.find({}).sort('i')
    # lista = await cursor.to_list(length=1)
    # for document in lista:
    #     remedios.append(remedio_converter(document))


    # pacientes_encontrados = remedio_collection.find()

    # for paciente in pacientes_encontrados:
    
    return remedios