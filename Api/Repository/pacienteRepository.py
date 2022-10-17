import motor.motor_asyncio
from decouple  import config
from models.Paciente import Paciente
from utils.converterUtil import paciente_converter

MONGODB_URL = config("MONGODB_URL")
cliente  = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.TCC

paciente_collection = database.get_collection("paciente")

async def criar_paciente(paciente: Paciente) -> dict:
    paciente_criado = await paciente_collection.insert_one(paciente.__dict__)
    novo_paciente = await paciente_collection.find_one({"_id": paciente_criado.inserted_id })
    return novo_paciente

def listar_pacientes():
    pacientes_encontrados = paciente_collection.aggreagate([{}])

    pacientes = []
    for paciente in pacientes_encontrados:
        pacientes.append(paciente_converter(paciente))
    
    return pacientes