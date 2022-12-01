from array import array
import datetime
from models.Paciente import Paciente
from utils.converterUtil import paciente_converter
from repository.database import get_database


db = get_database()

def criar_paciente(paciente: Paciente) -> dict:
    paciente_criado = db["paciente"].insert_one({
            "nome" : paciente.nome,
            "idade" : paciente.idade,
            "peso" : paciente.peso,
            "altura" : paciente.altura,
        })
    novo_paciente = db["paciente"].find_one({"_id": paciente_criado.inserted_id })
    return paciente_converter(novo_paciente)

async def listar_vinculos(paciente:str, dia:datetime) -> array:


    
    pacientes = []
    
    cursor = db["paciente"].find({})
    for paciente in await cursor.to_list(length=1):
        pacientes.append(paciente_converter(paciente))
    
    return pacientes