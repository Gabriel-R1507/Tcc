import datetime
from models.Vinculo import Vinculo
from models.Paciente import Paciente
from utils.converterUtil import paciente_converter, vinculo_converter
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

def criar_vinculos(vinc: Vinculo) -> dict:
    created = db["vinculo"].insert_one(vinc.__dict__)
    new = db["vinculo"].find_one({"_id": created.inserted_id })
    return vinculo_converter(new)

def listar_vinculos(paciente:str):
    vinculos = []
    for vinculo in db["vinculo"].find({"paciente": paciente}):
        vinculos.append(vinculo_converter(vinculo))
    
    return vinculos